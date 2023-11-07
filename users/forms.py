from django import forms
from django.core.exceptions import ValidationError
import re

def validate_not_malicious(value):
    # Define patterns to check for malicious input
    patterns = [
        r'<script.*?>.*?</script>',   # Enhanced check for <script> tags
        r'drop\s+table',  # Naive check for SQL DROP TABLE statements
        # ... Add other patterns you're concerned about
        r'script',
        r'/\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))/ix',
    ]
    # Check each pattern against the input value
    for pattern in patterns:
        if re.search(pattern, value, re.IGNORECASE):
            raise ValidationError('Potential XSS or SQL injection detected. This is your final warning')

class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        validators=[validate_not_malicious],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search...'})
    )