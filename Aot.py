
import httpx
from user_agent import generate_user_agent

tgAotpy = 'Reset_Tool'
Aotpy = '\033[92m'
ObitoStuffs = '\033[0m'


def send_reset(user):
    try:
        headers = {
            "user-agent": generate_user_agent(),
            "x-ig-app-id": "936619743392459",
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": "missing",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/"
        }

        r = httpx.Client(http2=True, headers=headers, timeout=20).post(
            "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/", 
            data={"email_or_username": user}
        )
        
        contact = r.json().get('contact_point', 'No email found')
        return f"{Aotpy}[+] Reset sent to: {contact}{ObitoStuffs}"
    
    except Exception as e:
        return f"{Aotpy}[!] Error: {str(e)}{ObitoStuffs}"

def main():
    print(f"{Aotpy}{'─' * 40}{ObitoStuffs}")
    user = input(f"{Aotpy}[?] Enter Email/Username: {ObitoStuffs}")
    print(send_reset(user))

if __name__ == "__main__":
    main()
