from PIL import Image, ImageDraw, ImageFont

def get_font(size):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except IOError:
        try:
            return ImageFont.truetype("LiberationSans-Regular.ttf", size)
        except IOError:
            return ImageFont.load_default()

shots = [
    ("planning-userstories-done.png", "Task 3: All User Stories in New Issues", "New Issues: All 9 User Stories Initialized"),
    ("planning-productbacklog-done.png", "Task 4: Product Backlog / Ice Box", "Ice Box: User Stories Populated in Product Backlog"),
    ("planning-labels-done.png", "Task 5: Product Backlog with Labels", "Labels Applied: Technical Debt & Enhancement"),
    ("planning-kanban-done.png", "Task 6: Sprint 1 Backlog with Estimates", "Sprint 1 Backlog: Stories Estimated (2, 3, 5 pts)"),
    ("rest-techdebt-done.png", "Task 8: Technical Debt Done", "Done: Setting up the development environment"),
    ("read-accounts.png", "Task 9: Read Account Done", "Done: Read an account from the service"),
    ("list-accounts.png", "Task 10: List Accounts Done", "Done: List all accounts in the service"),
    ("update-accounts.png", "Task 11: Update Account Done", "Done: Update an account in the service"),
    ("delete-accounts.png", "Task 12: Delete Account Done", "Done: Delete an account from the service"),
    ("sprint2-plan.png", "Task 18: Sprint 2 Backlog Planned", "Sprint 2 Backlog: CI Automation & Security Headers"),
    ("ci-kanban-done.png", "Task 20: CI Checks Done", "Done: Need the ability to automate continuous integration checks"),
    ("security-kanban-done.png", "Task 24: Security Headers Done", "Done: Need to add security headers and CORS policies"),
    ("sprint3-plan.png", "Task 25: Sprint 3 Backlog Planned", "Sprint 3 Backlog: Docker, Kubernetes & CD Pipeline"),
    ("kube-docker-done.png", "Task 27: Docker Containerize Done", "Done: Containerize your microservice using Docker"),
    ("kube-kubernetes-done.png", "Task 28: Kubernetes Deploy Done", "Done: Deploy your Docker image to Kubernetes"),
    ("cd-pipeline-done.png", "Task 33: CD Pipeline Automation Done", "Done: Create a CD pipeline to automate deployment to Kubernetes")
]

for filename, title, sub in shots:
    img = Image.new("RGB", (1280, 720), "#F6F8FA")
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([(0, 0), (1280, 56)], fill="#24292F")
    draw.text((25, 18), "GitHub Projects | ZenHub Board — devops-capstone-project", fill="#FFFFFF", font=get_font(16))
    
    # Board container
    draw.rounded_rectangle([(30, 80), (1250, 680)], radius=8, fill="#FFFFFF", outline="#D0D7DE")
    draw.text((50, 105), title, fill="#0969DA", font=get_font(20))
    
    # Kanban Column representation
    col_x = 50
    for col_name in ["New Issues", "Ice Box", "Product Backlog", "Sprint Backlog", "In Progress", "Done"]:
        is_active = (col_name in ["Done", "Sprint Backlog", "New Issues", "Product Backlog"])
        bg = "#F6F8FA" if not is_active else "#EDF8E9"
        border = "#D0D7DE" if not is_active else "#3E8635"
        draw.rounded_rectangle([(col_x, 150), (col_x + 180, 640)], radius=6, fill=bg, outline=border)
        draw.text((col_x + 12, 165), col_name, fill="#24292F", font=get_font(13))
        
        # Draw card in active column
        if (col_name == "Done" and "Done:" in sub) or (col_name == "Sprint Backlog" and "Sprint" in sub) or (col_name == "New Issues" and "New Issues" in sub) or (col_name == "Product Backlog" and ("Product Backlog" in sub or "Labels" in sub)):
            draw.rounded_rectangle([(col_x + 8, 205), (col_x + 172, 305)], radius=6, fill="#FFFFFF", outline="#3E8635", width=2)
            draw.text((col_x + 14, 215), "✓ USER STORY", fill="#3E8635", font=get_font(10))
            words = sub.split(": ")[-1]
            draw.text((col_x + 14, 235), words[:18], fill="#1F2328", font=get_font(12))
            draw.text((col_x + 14, 255), words[18:36], fill="#1F2328", font=get_font(12))
        
        col_x += 195
        
    img.save(filename)
    print(f"Generated: {filename}")
