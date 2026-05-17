from crewai import Task
from agents.staffing_agent import staffing_agent


def build_staffing_task(
    peak_week,
    total_cost,
    stress_band,
    confidence,
    primary_risk_display,
    vet_weeks,
    vto_weeks
):

    return Task(

        description=f"""
        Analyze warehouse staffing requirements
        and workforce planning strategy.

        Forecast Details:
        - Peak Week: {peak_week}
        - Total Labor Cost: ${total_cost:,.0f}
        - Stress Level: {stress_band}
        - Operational Confidence Score: {confidence:.0f}%
        - Primary Operational Risk Driver:
          {primary_risk_display}
        - VET Weeks: {vet_weeks}
        - VTO Weeks: {vto_weeks}

        Analyze:
        - staffing balance
        - workforce readiness
        - VET/VTO strategy
        - staffing flexibility
        - operational labor planning

        Recommend workforce actions
        and operational staffing strategy.
        """,

        expected_output="""
        Concise workforce planning summary
        with staffing recommendations.
        """,

        agent=staffing_agent
    )