from project import play_sound, load_image, get_balance
import tkinter
import pygame
import pytest
from unittest.mock import Mock, patch


def test_get_balance():
    # Mocking user input with patchers
    with patch.object(tkinter.simpledialog, "askinteger", return_value = 100):
        assert get_balance(Mock()) == 100
    
    with patch.object(tkinter.simpledialog, "askinteger", side_effect = [600, 200]):
        assert get_balance(Mock()) == 200
        
    with patch.object(tkinter.simpledialog, "askinteger", return_value = None):
        with pytest.raises(SystemExit):
            get_balance(Mock())
    

def test_load_image():
    tkinter.Tk()
    
    # Valid image file
    instance = tkinter.PhotoImage()
    assert isinstance(load_image("images/01.png"), type(instance))
    
    # Invalid image file
    with patch("tkinter.messagebox.showerror"):     # Mock messagebox to prevent GUI interaction
        with pytest.raises(SystemExit):
            load_image("images/invalid_image.png")
                
           
def test_play_sound():
    pygame.mixer.init()
    
    # Valid sound file
    valid_path = "sounds/roar.wav"
    instance = pygame.mixer.music.load(valid_path)
    valid_sound = play_sound(valid_path)
    assert isinstance(valid_sound, type(instance))
    
    # Invalid sound file
    with patch("tkinter.messagebox.showerror"):
        with pytest.raises(SystemExit):
            play_sound("sounds/invalid_sound.wav")