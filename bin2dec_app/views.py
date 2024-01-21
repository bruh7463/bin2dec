from django.shortcuts import render

from .forms import BinForm
from .own.bin2dec import bin2dec

def index(request):
	d_num = 0
	if request.method == "POST":
		form = BinForm(request.POST)
		if form.is_valid():
			b_num = request.POST['bin_num']
			d_num = bin2dec(b_num)

	else:
		form = BinForm()

	return render(request, 'bin2dec_app/index.html', {'form': form, 'd_num': d_num})