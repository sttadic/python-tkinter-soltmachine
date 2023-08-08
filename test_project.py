from project import play_sound, load_image, get_balance
import tkinter
import pytest
from unittest.mock import Mock, patch


def test_get_balance():
    # Mocking user input
    with patch.object(tkinter.simpledialog, 'askinteger', return_value = 100):
        assert get_balance(Mock()) == 100
    
    with patch.object(tkinter.simpledialog, 'askinteger', side_effect = [600, 200]):
        assert get_balance(Mock()) == 200
        
    with patch.object(tkinter.simpledialog, 'askinteger', return_value = None):
        with pytest.raises(SystemExit):
            get_balance(Mock())
    