pravo = 0
vniz = 0
def setup():
    size(800,600)
    
def draw():
    global pravo
    global vniz
    textSize(25)
    text("proide labirint", 300, 550);
    fill(180,249,255)
    ellipse(pravo,vniz,20,20)
    if keyPressed ==True:
        if key == "d":
            pravo = pravo + 1
    
    if keyPressed ==True:
        if key == 's':
            vniz = vniz + 1
            
    if keyPressed ==True:
        if key == "a":
            pravo = pravo - 1
            
    if keyPressed ==True:
        if key == "w":
            vniz = vniz - 1
            
    strokeWeight(5)
    point(280,520)
    point(280,600)
    line(280,520,280,600)
    
    point(480,520)
    point(480,600)
    line(480,520,480,600)
    line(280,520,480,520)
    
    point(30,0)
    point(30,60)
    line(30,0,30,60)
    point(65,60)
    line(30,60,65,60)
    point(65,23)
    line(65,60,65,23)
    point(100,23)
    line(65,23,100,23)

    

    
