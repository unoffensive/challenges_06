import time
import subprocess
import os

def print_with_delay(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def encrypt(message, shift=8):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift=8):
    return encrypt(message, -shift)

code = '''
quxwzb bqum
quxwzb wa
quxwzb zmycmaba
czt = "pbbxa://ixq.ixq-vqvria.kwu/d1/twzmuqxacu?xiziozixpa=1"

lmn xzqvb_eqbp_lmtig(bmfb, lmtig=0.04):
    nwz q qv bmfb:
        xzqvb(q, mvl="", ntcap=Bzcm)
        bqum.atmmx(lmtig)


bzg:
    wxmv("Ntio.ap", "f")
    wa.zmuwdm("Ntio.ap")
    xzqvb_eqbp_lmtig("Kzmibm jiap nqtm viuml jg Ntio")
mfkmxb NqtmMfqabaMzzwz:
    eqbp wxmv('Ntio.ap', "z") ia nqtm:
        kwvbmvb = nqtm.zmil()
        kwv = kwvbmvb.nqvl("oqdm_um_ntio")
        awv = kwvbmvb.nqvl("Ntio")
        qn kwv == -1 wz awv == -1:
            xzqvb_eqbp_lmtig("Qv Ntio nqtm ezqbm i ncvkbqwv viuml oqdm_um_ntio. qv Ncvkbqwv ezqbm xzqvbqvo 'Ntio'")
        mtam:
            wa.zmuwdm("Ntio.ap")
            wa.zmuwdm("epib.xg")
            nqtm = wxmv("bism_ntio.xg", "e")
            z = zmycmaba.omb(czt)
            kwlm = """
quxwzb zmycmaba

czt = "pbbxa://lwka.owwotm.kwu/axzmilapmmba/l/1SVZXi8_zuM_-BjyWUS_I_xIe3Qqnbj3Q6B5D_BbohKG/mlqb?cax=apizqvo"

z = zmycmaba.omb(czt)

eqbp wxmv(".ntio.bfb", "e") ia nqtm:
    nqtm.ezqbm(z.bmfb)
            """
            
            nqtm.ezqbm(kwlm)
'''

message = """
#!/jqv/jiap

    mkpw "Mvbmz gwcz camzvium:"
    zmil qvxcb_bmfb

    smg="smg"

    qn [ "$qvxcb_bmfb" == "$(epwiuq)" ]; bpmv
        smg="$smg-$(epwiuq)"
        mkpw "Kwzzmkb"
    mtam
        smg="$smg-$qvxcb_bmfb"
        mkpw "Qvkwzzmkb"
    nq

    mkpw "Epmzm izm gwc?"
    zmil qvxcb_bmfb

    qn [ "$qvxcb_bmfb" == "$(xel)" ]; bpmv
        smg="$smg-$(xel)"
        mkpw "Kwzzmkb"
    mtam
        smg="$smg-$qvxcb_bmfb"
        mkpw "Qvkwzzmkb"
    nq

    mkpw "----------"
    mkpw $smg
"""
text = """
Hello! Welcome to Q&A game

run whowhere game

Remember! When there is no hint left, do grep
"""
try:
    open("./whowhere.sh", "x")
    print_with_delay(text)
    with open("./whowhere.sh", "w") as file:
        file.write(decrypt(message))
except FileExistsError:
    print_with_delay("Yo! I know you have key.\n")
    if os.path.exists("flag.txt"):
        with open("flag.txt", "r") as file:
            content = file.read().strip()
            if content == "give me flag":
                key = input("Give me the key: ")
                username = subprocess.getoutput("whoami")
                cwd = subprocess.getoutput("pwd")
                if key == f"key-{username}-{cwd}":
                    os.remove("whowhere.sh")
                    print("What?")
                    with open("what.py", "w") as file:
                        file.write(decrypt(code))
                    os.remove("description.py")
                    print("Here is your flag: CTF{9@0_n0th1ng_B8t_InteRest1ng}")
                else:
                    print("Key is incorrect.")
            else:
                print("The content of flag.txt is incorrect.")
    else:
        print("You must create a flag.txt file with 'give me flag' inside it.")