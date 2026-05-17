from crewai import Task
from agents.executive_agent import executive_agent


def build_executive_task(
    peak_week,
    total_cost,
    stress_band,
    confidence_score,
    primary_risk_display,
    vet_weeks,
    vto_weeks,
    memory_context
):

    return Task(

        description=f"""
        You are the Executive Operations Intelligence Coordinator.

        Combine outputs from:
        - forecasting analysis
        - operational risk monitoring
        - labor cost analysis
        - workforce staffing strategy
        - workload stability assessment
        - VET/VTO workforce planning

        Relevant Historical Operational Memory:

        {memory_context}

        Current Operational Metrics:

        - Peak workload week: {peak_week}
        - Projected labor impact: ${total_cost:,.0f}
        - Operational stress level: {stress_band}
        - Operational confidence score: {confidence_score}%
        - Primary operational risk: {primary_risk_display}
        - Total VET weeks: {vet_weeks}
        - Total VTO weeks: {vto_weeks}

        Create a concise executive operational intelligence briefing.

        Requirements:
        - maximum 6 bullet points
        - executive business language
        - concise operational tone
        - avoid filler or repetition
        - focus on actionable operational insight
        - highlight staffing risks if present
        - highlight labor cost concerns if present
        - mention workforce readiness
        - mention workload stability
        - mention operational confidence
        - do NOT use numbering
        - do NOT write long paragraphs
        - each bullet should be one concise sentence
        - avoid generic AI phrases
        - avoid motivational language
        - avoid speculative recommendations
        - avoid repeating the same operational insight
        - prioritize concise executive communication

        The summary should sound like an enterprise warehouse
        operations intelligence platform used by senior leadership.
        """,

        expected_output="""
        Concise executive operational intelligence briefing
        using short executive bullet points.
        """,

        agent=executive_agent
    )