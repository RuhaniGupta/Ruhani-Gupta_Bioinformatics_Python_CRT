'''Consider you are a HR Operations manager in Vignan Software Solutions,you will be receiving Applications from the candidates for multiple roles,you are having a list of JobRoles write a program
1. To view the Candidates applications
2. Based on your evaluation on CV of a candidate,Send a message to a candidate to update whether his/her CV is shortlisted or not
3. Scheduled an Interviewed for the Particular Shortlisted Candidates
4.Send a message to a candidate to update the status of their Level-1 Interview Feedback & inform whether they are qualified or not for further level interview
5.Send an Offer letter to  the Shortlisted(Level-3) Candidates'''
class Candidate:
    def __init__(self, name, job_role):
        self.name = name
        self.job_role = job_role
        self.shortlisted = False
        self.level1_qualified = False
        self.level3_qualified = False

class HRManager:
    def __init__(self):
        self.candidates = []
        self.job_roles = ["Software Engineer", "Data Analyst", "QA Engineer", "HR Executive"]

    def add_candidate(self, name, job_role):
        if job_role in self.job_roles:
            self.candidates.append(Candidate(name, job_role))
        else:
            print(f"Job role '{job_role}' not available.")

    def view_applications(self):
        print("\nCandidate Applications:")
        for c in self.candidates:
            print(f"Name: {c.name}, Job Role: {c.job_role}")

    def shortlist_candidate(self, name, status):
        for c in self.candidates:
            if c.name == name:
                c.shortlisted = status
                msg = "shortlisted" if status else "not shortlisted"
                print(f"Message to {c.name}: Your CV is {msg}.")
                return
        print("Candidate not found.")

    def schedule_interview(self, name):
        for c in self.candidates:
            if c.name == name and c.shortlisted:
                print(f"Interview scheduled for {c.name}.")
                return
        print("Candidate not found or not shortlisted.")

    def level1_feedback(self, name, qualified):
        for c in self.candidates:
            if c.name == name and c.shortlisted:
                c.level1_qualified = qualified
                msg = "qualified" if qualified else "not qualified"
                print(f"Message to {c.name}: You are {msg} for the next level interview.")
                return
        print("Candidate not found or not shortlisted.")

    def send_offer_letter(self, name):
        for c in self.candidates:
            if c.name == name and c.level3_qualified:
                print(f"Offer letter sent to {c.name}. Congratulations!")
                return
        print("Candidate not found or not qualified for offer.")
hr = HRManager()
hr.add_candidate("Alice", "Software Engineer")
hr.add_candidate("Bob", "Data Analyst")
hr.add_candidate("Charlie", "QA Engineer")

hr.view_applications()
hr.shortlist_candidate("Alice", True)
hr.shortlist_candidate("Bob", False)
hr.schedule_interview("Alice")
hr.level1_feedback("Alice", True)
for c in hr.candidates:
    if c.name == "Alice":
        c.level3_qualified = True

hr.send_offer_letter("Alice")
