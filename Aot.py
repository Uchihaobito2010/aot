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
    
    if user.lower() == "owner":
        print(f"{Aotpy}[+] Owner Telegram: t.me/Aotpy{ObitoStuffs}")
    else:
        print(send_reset(user))