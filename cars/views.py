from django.shortcuts import render

def carsView(request):
    return render(
        request,
        'cars.html', 
        {'cars': 
            {'model': 'Astra 2.0'},
        'cars': 
            {'model': 'Astra 2.0'},
        'cars': 
            {'model': 'Astra 2.0'},
        'cars': 
            {'model': 'Astra 2.0'},
        'cars': 
            {'model': 'uno 2.0'},
        }
    )