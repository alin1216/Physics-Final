scene.userzoom=False
plane = box(pos=vector(0,0,0), length=7, height=5, width=5, texture="https://i.guim.co.uk/img/media/3d2ae1c487cd56144d4df80ca9b4d713cd91f9a8/0_444_4721_2832/master/4721.jpg?width=620&dpr=2&s=none&crop=none")
view = scene.camera.pos=vector(0,0,1)
light = distant_light(direction=vec(0,0,-1),color=color.white)

#parameters
L = 1.2 #total length
N = 15 #number of spheres
M = .05 # mass
k = 5 # spring constant 
A = 0 #amplitude
c = .01 #damping constant
t = 0
dt = .0001
T = 0
w = 0

amp_graph = graph(xtitle='Time', ytitle='Y Position', height=250, width=350, align='left')
ball7_graph = gcurve(color=color.blue, graph=amp_graph)
ball4_graph = gcurve(color=color.orange, graph=amp_graph)
freq_graph = graph(xtitle = 'Tension', ytitle = 'Frequency', xmin=0, xmax=150, ymin=0, ymax=20, height=250, width=350, align='left')
fd = gdots(color=color.black, graph=freq_graph)

def current_w():
    global w, T
    w = sqrt((k/M)-(c/(2*M))^2)
    T = 2*pi/w
    
def tot_mass():
    global M
    M = mass_slider.value/N
    mass_title.text=mass_slider.value
    current_w()
 
mass_slider = slider (bind=tot_mass, min=.05, value=.05, max=1, pos=scene.append_to_caption('Mass''\n'), disabled=False, step=.05)
mass_title = wtext(text=M)

def tot_k(): 
    global k 
    k = (tension_slider.value/(N-1))*20
    tension_title.text=tension_slider.value
    current_w()

tension_slider = slider (bind=tot_k, min=5, value=5, max=100, pos=scene.append_to_caption('\n''Tension''\n'), disabled=False, step=5)
tension_title = wtext(text=k)

def pulldistance():
    global A
    A = pullslider.value 
    distance_title.text=pullslider.value

pullslider = slider (bind=pulldistance, min=0, max=.175, pos=scene.append_to_caption('\n''Distance''\n'), disabled=False, step=.01)
distance_title = wtext(text=A)


left = vector(-L/2,0,0)
right = left+vector(L,0,0)
ds = vector(1,0,0)*L/(N-1)
R = L/(N*5)
    
pluck = False
def begin():
    global pluck 
    pluck = not pluck
    global t
    t =1
    start.disabled=True
    end.disabled=False
    pullslider.disabled=True
    mass_slider.disabled=True
    tension_slider.disabled=True
    fd.plot(k, 1/T)

 

    
def reset():
    global pluck
    global t
    t = 100
    pluck = not pluck
    start.disabled=False
    end.disabled=True
    pullslider.disabled=False
    mass_slider.disabled=False
    tension_slider.disabled=False
    ball7_graph.delete()
    ball4_graph.delete()
    

    

    

start = button(bind=begin, text='start', pos=scene.title_anchor, disabled=False)
end = button(bind=reset, text="reset", pos=scene.title_anchor, disabled=True)

balls = []
    
for i in range(N):
    balls = balls + sphere(pos=left+i*ds, radius=R, color=color.red, m=M, F=vector(0,0,0), p=vector(0,0,0))
balls[7].color = color.blue
balls[4].color = color.orange
    
springs = []
    
for i in range(N-1):
    springs = springs + cylinder(pos=left+i*ds, axis=ds, radius=(R/2))
    

stretch_length = .95*L/(N-1)
F_spring=-k*(mag(springs[i-1].axis)-stretch_length)*norm(springs[i-1].axis)+k*(mag(springs[i].axis)-stretch_length)*norm(springs[i].axis)
F_damp=-c*(mag(springs[i-1].axis)-stretch_length)*norm(springs[i-1].axis)+c*(mag(springs[i].axis)-stretch_length)*norm(springs[i].axis)
                            


while t<1000:
    rate(1000000)
    
            
    
    if pluck:
        if t<T:
            balls[7].pos.y = -A*cos(w*t)
            balls[7].p = vector(0,0,0)   
                 
        v = balls[i].p/balls[i].m
        damping = -c*v
        for i in range(1,N-1):
            balls[i].F = -k*(mag(springs[i-1].axis)-stretch_length)*norm(springs[i-1].axis)+k*(mag(springs[i].axis)-stretch_length)*norm(springs[i].axis) + damping
                
        for ball in balls:
            ball.p = ball.p + ball.F*dt
            ball.pos = ball.pos + ball.p*dt/ball.m
                    
        for i in range(N-1):
            springs[i].axis = balls[i+1].pos - balls[i].pos
            springs[i].pos = balls[i].pos
                
        ball7_graph.plot(t, balls[7].pos.y)
        ball4_graph.plot(t, balls[4].pos.y)
    
    else:
        for i in range(1,7):
            balls[i].pos.y = (balls[i-1].pos.y - (A/((N-1)/2)))
            balls[7].pos.y = -A
        for i in range(8,N-1):
            balls[i].pos.y = (balls[i-1].pos.y + (A/((N-1)/2)))
        for i in range(N-1):
            springs[i].axis = balls[i+1].pos - balls[i].pos
            springs[i].pos = balls[i].pos
        for ball in balls:
            ball.F = vector(0,0,0)  
    
    t=t+dt                 

