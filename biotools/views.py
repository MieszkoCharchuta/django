import random
from Bio.Seq import Seq
from django.shortcuts import render

from . import utils
from .forms import SeqContentForm, RevCompForm, RandomDNAForm


def seqcontent_view(request):
    if request.method == "POST":
        # formularz został wysłany
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data["sequence"]
            word_size = form.cleaned_data["word_size"]
            d = utils.count_words(seq, word_size)
            return render(
                request,
                "biotools/seqcontent.html",
                {"results": d, "query_length": len(seq)},
            )
    else:
        form = SeqContentForm()  # Utworzenie pustego formularza

    return render(request, "biotools/seqcontent.html", {"form": form})


def revcomp_view(request):
    if request.method == "POST":
        form = RevCompForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["sequence"]
            method = form.cleaned_data["method"]
            header = data["header"] or "Original Sequence"
            seq = data["sequence"]

            # Apply the selected method
            if method == "reverse":
                result_seq = seq[::-1]
                result_header = f"Reverse of: {header}"
            elif method == "complement":
                result_seq = str(Seq(seq).complement())
                result_header = f"Complement of: {header}"
            elif method == "reverse_complement":
                result_seq = str(Seq(seq).reverse_complement())
                result_header = f"Reverse Complementary of: {header}"

            # Wrapping sequences
            query_seq_wrapped = utils.wrap_sequence(seq)
            result_seq_wrapped = utils.wrap_sequence(result_seq)

            return render(
                request,
                "biotools/revcomp.html",
                {
                    "query_header": header,
                    "query_sequence": query_seq_wrapped,
                    "result_header": result_header,
                    "result_sequence": result_seq_wrapped,
                },
            )
    else:
        form = RevCompForm()
    return render(request, "biotools/revcomp.html", {"form": form})

def random_dna_view(request):
    if request.method == "POST":
        form = RandomDNAForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data["length"]
            probs = [
                form.cleaned_data["prob_A"],
                form.cleaned_data["prob_T"],
                form.cleaned_data["prob_C"],
                form.cleaned_data["prob_G"],
            ]
            nucleotides = ["A", "T", "C", "G"]
            sequence = "".join(
                random.choices(nucleotides, weights=probs, k=length)
            )

            # Wrapping sequence for better display
            wrapped_sequence = "\n".join(
                sequence[i : i + 80] for i in range(0, len(sequence), 80)
            )

            return render(
                request,
                "biotools/random_dna.html",
                {"form": form, "sequence": wrapped_sequence},
            )
    else:
        form = RandomDNAForm()

    return render(request, "biotools/random_dna.html", {"form": form})