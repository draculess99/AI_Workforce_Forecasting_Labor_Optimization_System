from crewai import Task

def build_risk_task(
    peak_week,
    total_cost,
    stress_band,
    primary_risk_display
):

    return Task(

        description=f"""
        Analyze warehouse operational risks.

        Forecast Summary:
        - Peak Week: {peak_week}
        - Total Labor Cost: ${total_cost:,.0f}
        - Stress Level: {stress_band}
        - Primary Risk Driver: {primary_risk_display}

        Evaluate:
        - operational instability
        - labor volatility
        - workforce stress
        - staffing risk exposure
        """,

        expected_output="""
        Concise operational risk summary
        in executive business language.
        """
    )