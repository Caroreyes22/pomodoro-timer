from django.shortcuts import render

def timer(request):
    return render(request, "pomodoro/timer.html")

def consejos(request):
    tips = [
        "Divide tus sesiones de estudio en bloques de 25 minutos.",
        "Apaga las notificaciones mientras estudias.",
        "Tómate 5 minutos para estirarte cada hora.",
        "Prioriza las tareas más difíciles al inicio del día.",
        "Usa música suave o silencio total para concentrarte mejor.",
    ]
    return render(request, "pomodoro/consejos.html", {"tips": tips})
