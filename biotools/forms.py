import re

from django import forms


class SeqContentForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter a sequence",
                "class": "form-control",
            }
        ),
        required=True,
        min_length=5,
    )
    word_size = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        return sequence.upper()

    def clean_word_size(self):
        word_size = self.cleaned_data["word_size"]
        if word_size < 1:
            raise forms.ValidationError("Word size must be greater than or equal to 1.")
        return word_size

    def clean(self):
        sequence = self.cleaned_data["sequence"]
        word_size = self.cleaned_data["word_size"]
        if word_size and sequence:
            if word_size > len(sequence):
                raise forms.ValidationError(
                    "Sequence must be longer than or equal to word size."
                )


class RevCompForm(forms.Form):
    sequence = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Enter a sequence", "class": "form-control"}
        ),
        required=True,
        min_length=5,
    )
    method = forms.ChoiceField(
        choices=[
            ("reverse", "Reverse"),
            ("complement", "Complement"),
            ("reverse_complement", "Reverse Complement"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        header = ""
        if sequence.startswith(">"):
            header, sequence = sequence.split("\n", 1)
            header = header.strip()
        sequence = re.sub(r"\s+", "", sequence.upper())
        return {"header": header, "sequence": sequence}

from django import forms

class RandomDNAForm(forms.Form):
    length = forms.IntegerField(
        required=True,
        min_value=20,
        max_value=10000,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter length (20-10000)"}
        ),
    )
    prob_A = forms.FloatField(
        required=False,
        min_value=0,
        max_value=1,
        initial=0.25,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Probability of A"}
        ),
    )
    prob_T = forms.FloatField(
        required=False,
        min_value=0,
        max_value=1,
        initial=0.25,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Probability of T"}
        ),
    )
    prob_C = forms.FloatField(
        required=False,
        min_value=0,
        max_value=1,
        initial=0.25,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Probability of C"}
        ),
    )
    prob_G = forms.FloatField(
        required=False,
        min_value=0,
        max_value=1,
        initial=0.25,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Probability of G"}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        probs = [
            cleaned_data.get("prob_A", 0.25),
            cleaned_data.get("prob_T", 0.25),
            cleaned_data.get("prob_C", 0.25),
            cleaned_data.get("prob_G", 0.25),
        ]
        if sum(probs) != 1:
            raise forms.ValidationError("The sum of probabilities must equal 1.")
        return cleaned_data
