import pymsgbox

def check_strings(*strings) -> bool:
    """ Verifica se todos os parâmetros são strings e não estão vazias
    Args:
        *strings: strings para serem válidadas.
    """
    for string in strings:
        if string is None or type(string) != str or string == '' or len(string) < 1:
            return False
    return True

def inputbox_text(title: str, prompt: str, default_value: str = '') -> str:
    return pymsgbox.prompt(prompt, title, default_value)

def inputbox_password(title: str, prompt: str) -> str:
    return pymsgbox.password(prompt, title)

def inputbox_yes_no(title: str, prompt: str, buttons: list[str] = ('Sim', 'Não')) -> str:
    return pymsgbox.confirm(prompt, title, buttons=list(buttons)) == buttons[0]
