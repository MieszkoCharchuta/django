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

    def clean_sequence(self):
        sequence = self.cleaned_data["sequence"]
        header = ""
        if sequence.startswith(">"):
            header, sequence = sequence.split("\n", 1)
            header = header.strip()
        sequence = re.sub(r"\s+", "", sequence.upper())
        return {"header": header, "sequence": sequence}
