import PySimpleGUI as sg
import pyperclip
from argon2 import PasswordHasher
from manager import get_key, add_entry, del_entry, search_entry, list_entry, repeated_pass, repeated_site
from pass_gen import pass_generator, decrypt

sg.theme('BlueMono')  # Add a touch of color to UI

# All the stuff inside your first window, main window
layout = [
    [sg.Image('ui.png', size=(443, 122))],
    [
        sg.Text('Website'),
        sg.InputText('.com', size=21, key='web'),
        sg.Button('Get', size=7),
        sg.Button('List', size=7)
    ],
    [
        sg.Text('Email/Username'),
        sg.InputText('@gmail.com', size=27, key='mail'),
        sg.Button(key='Copy_mail', size=7, button_text='Copy')
    ],
    [
        sg.Text('Password'),
        sg.InputText(size=16, key='pass'),
        sg.Combo(values=(10, 11, 12, 13, 14), size=2, key='len'),
        sg.Button('Generate', size=7),
        sg.Button(key='Copy_pass', size=7, button_text='Copy')
    ],
    [sg.Button('Add', size=28), sg.Button('Del', size=13)]
]


def passcode():
    # Create the main window
    window = sg.Window('PassCode Password Manager', layout, size=(400, 300), margins=(20, 10))

    # Enter master password
    mp = sg.popup_get_text('Enter your master password:', size=(33, 20), title='PassCode')
    ph = PasswordHasher()
    try:
        if ph.verify(get_key('master_key_hash', 'master'), mp) is True:
            sg.popup_annoying('Welcome back!')
    except Exception:
        sg.popup_annoying('Wrong master password. Program exiting')
        window.close()

    # Create second window with list of entries
    def list_entries_window():
        list_entries_layout = [[sg.Listbox(list_entry(), size=(50, 50), enable_events=True, key='list',
                                           select_mode='single', bind_return_key=True)]]

        list_entries_window = sg.Window('List of your entries', list_entries_layout, size=(300, 400), margins=(20, 10),
                                        auto_size_text=True, resizable=True)

        while True:
            event, values = list_entries_window.read()
            if event == sg.WIN_CLOSED:  # If user closes window
                break
            if event == 'list' and len(values['list'][0][0]):
                window['web'].update(values['list'][0][0])
                result = search_entry(window['web'].get())
                window['mail'].update(value=decrypt(get_key('secret_key', 'secret'), result[0][1]))
                window['pass'].update(value=decrypt(get_key('secret_key', 'secret'), result[0][2]))
                sg.popup_annoying('Website was selected')
                break
        list_entries_window.close()

    # Create an event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # If user closes window
            break
        elif event == 'Get':  # If user clicks Get
            result = search_entry(window['web'].get())
            if len(result) > 0:
                window['web'].update(value=result[0][0])
                window['mail'].update(value=decrypt(get_key('secret_key', 'secret'), result[0][1]))
                window['pass'].update(value=decrypt(get_key('secret_key', 'secret'), result[0][2]))
            else:
                sg.popup_annoying('No such website')
        elif event == 'List':  # If user clicks List
            list_entries_window()
        elif event == 'Add':  # If user clicks Add
            if len(window['web'].get()) < 5:
                sg.popup_annoying('Please enter website name')
            elif repeated_site(window['web'].get()) is True:
                sg.popup_annoying('You have password to this site')
            elif len(window['mail'].get()) < 11:
                sg.popup_annoying('Please enter your email or username')
            elif len(window['pass'].get()) < 10:
                sg.popup_annoying('Weak password! Please use generator')
            elif repeated_pass(window['pass'].get()) is True:
                sg.popup_annoying(
                    "You already use this password on another site. Repeating the password is not allowed")
            else:
                add_entry(window['web'].get(), window['mail'].get(), window['pass'].get())
                sg.popup_annoying('Entry added')
        elif event == 'Del':
            if len(window['web'].get()) == 0:
                sg.popup_annoying('Please enter the name of the website you want to delete')
            elif del_entry(window['web'].get()) == 0:
                sg.popup_annoying('No such website')
            else:
                del_entry(window['web'].get())
                sg.popup_annoying('The entry has been deleted')
        elif event == 'Generate':  # If user clicks Generate
            if window['len'].get() in [10, 11, 12, 13, 14]:
                window['pass'].update(value=pass_generator(window['len'].get()))
            else:
                sg.popup_annoying('Select password length')
        elif event == 'Copy_pass':  # If user clicks Copy_pass
            if len(window['pass'].get()) >= 10:
                pyperclip.copy(window['pass'].get())
            elif len(window['pass'].get()) == 0:
                sg.popup_annoying('No password')
            else:
                sg.popup_annoying('Password too short!')
        elif event == 'Copy_mail':  # If user clicks Copy_mail
            if len(window['mail'].get()) == 0:
                sg.popup_annoying('No mail')
            pyperclip.copy(window['mail'].get())
    window.close()
