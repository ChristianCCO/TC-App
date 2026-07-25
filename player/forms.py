from django import forms
from .models import Player, Set


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['player_2', 'player_1_games', 'player_2_games']
        widgets = {
            'player_2': forms.Select(attrs={'class': 'sub-name'}),
            'player_1_games': forms.NumberInput(attrs={'class': 'sub-number'}),
            'player_2_games': forms.NumberInput(attrs={'class': 'sub-number'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        player = user.player
        self.fields['player_2'].queryset = Player.objects.filter(circle=player.circle).exclude(user=user)
        self.fields['player_2'].empty_label = 'Opponent'
    
    def clean(self):
        cleaned_data = super().clean()
        games1 = cleaned_data.get('player_1_games')
        games2 = cleaned_data.get('player_2_games')

        if games1 is None or games2 is None:
            return cleaned_data
        
        if games1 > 7 or games2 > 7:
            raise forms.ValidationError('Please enter a valid score.')
        
        if games1 < 6 and games2 < 6:
            raise forms.ValidationError('Please enter a valid score.')
        
        if games1 == games2:
            raise forms.ValidationError('Please enter a valid score.')
        
        if games1 == 6 and games2 not in (0, 1, 2, 3, 4, 7):
            raise forms.ValidationError('Please enter a valid score.')
        
        if games2 == 6 and games1 not in (0, 1, 2, 3, 4, 7):
            raise forms.ValidationError('Please enter a valid score.')
        
        if games1 == 7 and games2 not in (5, 6):
            raise forms.ValidationError('Please enter a valid score.')
        
        if games2 == 7 and games1 not in (5, 6):
            raise forms.ValidationError('Please enter a valid score.')
        
        return cleaned_data