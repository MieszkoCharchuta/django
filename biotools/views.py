from Bio.Seq import Seq
from django.shortcuts import render

from . import utils
from .forms import SeqContentForm, RevCompForm


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
            header = data["header"] or "Original Sequence"
            seq = data["sequence"]
            rev_comp_seq = Seq(seq).reverse_complement()

            # Wrapping sequences
            query_seq_wrapped = utils.wrap_sequence(seq)
            rev_comp_seq_wrapped = utils.wrap_sequence(str(rev_comp_seq))

            return render(
                request,
                "biotools/revcomp.html",
                {
                    "query_header": header,
                    "query_sequence": query_seq_wrapped,
                    "revcomp_header": f"Reverse Complementary of: {header}",
                    "revcomp_sequence": rev_comp_seq_wrapped,
                },
            )
    else:
        form = RevCompForm()
    return render(request, "biotools/revcomp.html", {"form": form})
