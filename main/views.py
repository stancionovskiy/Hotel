import binascii
from hashlib import sha256
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
	return render(request, 'main/Royal Hotel.html', {'sign': ''})


@csrf_exempt
def check(request):
	def generator(m_shop, m_orderid, m_amount, m_curr, ):
		description = ""
		m_desc = binascii.b2a_base64(description.encode('utf8'))[:-1].decode()
		m_key = "GtCNMIh67SHBXcHV"
		list_of_value_for_sign = map(str, [m_shop, m_orderid, m_amount, m_curr, m_desc, m_key])
		result_string = ":".join(list_of_value_for_sign)
		sign_hash = sha256(result_string.encode())
		sign = sign_hash.hexdigest().upper()
		return sign

	standard = ("1013136080", "4", "500.00", "RUB", )
	love = ("1013136080", "3", "999.00", "RUB", )
	pro = ("1013136080", "2", "1399.00", "RUB", )
	vip = ("1013136080", "1", "1799.00", "RUB", )
	context = {
		'std': generator(*standard),
		'love': generator(*love),
		'pro': generator(*pro),
		'vip': generator(*vip),
	}
	return render(request, 'main/12.html', context)


def success(request):
	return HttpResponse('Платеж успешно прошел!')

def fail(request):
	return HttpResponse('Ошибка оплаты, что-то пошло не так!')

def event(request):
	return HttpResponse('Siski')
