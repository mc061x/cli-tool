from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent

def add_autocomplete_binding(binds: KeyBindings) -> None:
    @binds.add('tab')
    def _(event: KeyPressEvent):
        currentText = event.current_buffer.text
        if currentText.strip() != '' and event.current_buffer.suggestion != None:
            event.current_buffer.insert_text(event.current_buffer.suggestion.text)    
