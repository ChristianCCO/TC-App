🎾 Tennis Circle

A full-stack Django web application that allows users to create competitive tennis circles, submit match results, and track rankings using an ELO rating system.


👤 Authentication

• User signup, login, and logout
• Automatic Player creation

🧑‍🤝‍🧑 Circles (Groups)

• Users can create or join a Circle via invite link
• Each player belongs to exactly one Circle
• Matches are restricted within Circles

🎾 Match Submission

• Submit tennis set scores against other players
• Built-in validation for real tennis rules
• Prevents invalid or duplicate matches

✅ Match Confirmation System

• Opponent can confirm or reject submitted matches
• Only confirmed matches affect rankings
• Pending matches visible in dashboard

🏆 ELO Rating System

• Dynamic skill-based ranking
• Ratings update after each confirmed match
• Fair adjustments based on opponent strength

📊 Player Profiles

• View rating and match history
• Win/loss tracking

🧠 Tech Stack

• Frontend: Django Templates (HTML/CSS)
• Backend: Django (Python)
• Database: SQLite (dev) / PostgreSQL (prod-ready)
• Auth: Django built-in authentication

🏗️ Architecture Overview

• User → Django auth system
• Player → One-to-one extension of User
• Circle → Groups of players
• Set → Match records

⚙️ Key Concepts Implemented

• Relational data modeling
• Business logic validation (tennis scoring rules)
• Stateful workflows (pending → confirmed matches)
• ELO rating algorithm
• Access control and permissions

🔮 Future Improvements

• ELO graphs and visualizations
• Notifications for pending matches
• Mobile-friendly UI
• REST API (Django REST Framework)

📚 What I Learned

• Designing relational data models for real-world systems
• Implementing multi-user workflows and permissions
• Building a ranking system using ELO
• Structuring Django apps for scalability
