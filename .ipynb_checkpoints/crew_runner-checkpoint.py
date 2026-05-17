from crewai import Crew

# Agents
from agents.forecast_agent import forecast_agent
from agents.cost_agent import cost_agent
from agents.staffing_agent import staffing_agent
from agents.executive_agent import executive_agent

# Tasks
from tasks.forecast_task import build_forecast_task
from tasks.cost_task import build_cost_task
from tasks.staffing_task import build_staffing_task
from tasks.executive_task import build_executive_task

from memory_manager import (
    add_operational_memory,
    retrieve_relevant_memories
)


def run_operational_crew(
    result_df,
    stress_band,
    total_cost,
    peak_week,
    confidence_score,
    primary_risk_display,
    vet_weeks,
    vto_weeks
):

    # -----------------------------
    # Build Tasks
    # -----------------------------

    forecast_task = build_forecast_task(
        peak_week,
        total_cost,
        stress_band,
        confidence_score,
        primary_risk_display
    )

    cost_task = build_cost_task(
        peak_week,
        total_cost,
        stress_band,
        confidence_score,
        primary_risk_display
    )

    staffing_task = build_staffing_task(
        peak_week,
        total_cost,
        stress_band,
        confidence_score,
        primary_risk_display,
        vet_weeks,
        vto_weeks
    )

    executive_task = build_executive_task(
        peak_week,
        total_cost,
        stress_band,
        confidence_score,
        primary_risk_display,
        vet_weeks,
        vto_weeks
    )

    # -----------------------------
    # Build Crew
    # -----------------------------

    crew = Crew(
        agents=[
            forecast_agent,
            cost_agent,
            staffing_agent,
            executive_agent
        ],

        tasks=[
            forecast_task,
            cost_task,
            staffing_task,
            executive_task
        ],

        verbose=True
    )

    # -----------------------------
    # Execute Crew
    # -----------------------------

    if vet_weeks > vto_weeks:
        memory_type = "VET"
    else:
        memory_type = "VTO"

    past_memories = retrieve_relevant_memories(
        action_type=memory_type
    )

    memory_context = "\n".join([
        f"- {m['summary']}"
        for m in past_memories
    ])

    result = crew.kickoff()

    return str(result)