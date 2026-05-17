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
        
        You MUST return ONLY the following format.
        
        Do NOT include bullet points.
        Do NOT include introductions.
        Do NOT include explanations outside this structure.
        Do NOT include extra commentary.
        
        Recommended Action:
        <VET / VTO / Maintain Staffing>
        
        Staffing Risk Level:
        <Low / Medium / High>
        
        Operational Concern:
        <one concise operational concern>
        
        Operational Reason:
        <one concise sentence>
        
        Workforce Recommendation:
        <one concise sentence>""",

        expected_output="""
        Recommended Action:
        <VET / VTO / Maintain Staffing>
        
        Staffing Risk Level:
        <Low / Medium / High>
        
        Operational Concern:
        <operational concern>
        
        Operational Reason:
        <one concise sentence>
        
        Workforce Recommendation:
        <one concise sentence>
        """,

        agent=staffing_agent
    )