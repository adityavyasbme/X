from src.infrastructure import openAI
from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/coverLetterPrompt")
def coverLetterPrompt(job_description: str,
                      resume: str = None
                      ):
    base = f"""
    write me a cover letter for this job description
    '''
    {job_description}
    '''
    Using the detailed information provided generate a customized cover letter.
    The job description lays out the specific roles,
    responsibilities, and required expertise for the open position.
    The generated cover letter should appropriately highlight
    the individual's fit for the job, emphasise their key
    skills and experiences, and prompt for the start of
    a professional conversation. Remember to generate text that
    maintains a formal and professional tone, and matches the candidate's
    experiences with the requirements of the job description in the most
    optimal way.
    Write as me.
    """
    if resume:
        return f"""
        Here's my resume
        '''
        {resume}
        '''
        The resume includes the candidate's educational background,
        skills, and experiences related to specific industries and roles.
        """ + base
    else:
        return base


@router.get("/api/coverLetterPromptResponse")
def coverLetterPromptResponse(
        api_key: str,
        job_description: str,
        resume: str = None,
        model_name: str = "gpt-3.5-turbo") -> Dict[str, str]:
    return openAI.get_response(api_key=api_key,
                               content=coverLetterPrompt(
                                   resume=resume,
                                   job_description=job_description),
                               model_name=model_name
                               )
