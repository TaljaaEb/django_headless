from django.http import JsonResponse

def run_task_view(request):
    # Your core Python logic goes here
    # Example: result = my_python_function()
    
    data = {
        "status": "success",
        "message": "Backend Python code executed successfully via curl!",
        "parameters_received": dict(request.GET)
    }
    return JsonResponse(data)
