
name=input('Type Your Name:')
designation =input('Type Your designation :')
bio=input('Type Your bio:')
image=input('Type Your image url:')
website=input('Type Your website:')
github=input('Type Your github:')
email=input('Type Your email:')
linkedin=input('Type Your linkedin:')



#  *** File Handling Operation ***
file = open('Intro_card.html', 'w+')
file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {{
            background: #f8f9fa;
            height: 100vh;
        }}

        .profile-card {{
            width: 100%;
            max-width: 430px;
            border: none;
            border-radius: 20px;
            overflow: hidden;
        }}

        .profile-header {{
            height: 120px;
            background: linear-gradient(135deg, #212529, #000000);
        }}

        .profile-img {{
            width: 100px;
            height: 100px;
            object-fit: cover;
            border: 4px solid #fff;
            margin-top: -50px;
        }}

        .social a {{
            width: 42px;
            height: 42px;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            border-radius: 50%;
            text-decoration: none;
        }}
    </style>

    <!-- Bootstrap Icons -->
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
</head>

<body class="d-flex justify-content-center align-items-center">

    <div class="card profile-card shadow-lg">

        <!-- Header -->
        <div class="profile-header"></div>

        <div class="card-body text-center px-4 pb-4">

            <!-- Profile Image -->
            <img src="{image}"
                 class="profile-img rounded-circle shadow"
                 alt="Profile">

            <!-- Name -->
            <h2 class="fw-bold mt-3 mb-1">{name}</h2>

            <!-- Profession -->
            <span class="badge bg-dark px-3 py-2 fs-6">
                {designation}
            </span>

            <!-- Bio -->
            <p class="text-secondary mt-3">
                {bio}
            </p>

            <hr>

            <!-- Social -->
            <div class="social d-flex justify-content-center gap-3 mb-4">

                <a href="{github}" class="btn btn-dark">
                    <i class="bi bi-github"></i>
                </a>

                <a href="{linkedin}" class="btn btn-primary">
                    <i class="bi bi-linkedin"></i>
                </a>

                <a href="{website}" class="btn btn-success">
                    <i class="bi bi-globe"></i>
                </a>

            </div>

            <!-- Buttons -->
            <div class="d-grid gap-2">
                <a href="mailto:{email}" class="btn btn-dark">
                    Contact Me
                </a>

                <a href="resume" class="btn btn-outline-dark">
                    Download Resume
                </a>
            </div>

        </div>

    </div>

</body>
</html>


 """)
print('updated successfully')
file.close()