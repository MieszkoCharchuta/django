from django.shortcuts import render

from . import utils
from .forms import SeqContentForm


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
        # formularz został wysłany
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data["sequence"]
            word_size = form.cleaned_data["word_size"]
            d = utils.count_words(seq, word_size)
            return render(
                request,
                "biotools/revcomp.html",
                {"results": d, "query_length": len(seq)},
            )
    else:
        form = SeqContentForm()  # Utworzenie pustego formularza

    return render(request, "biotools/revcomp.html", {"form": form})
