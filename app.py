# country codes module
import os  # os module
import sys  # sys module


# The class creates a window with a text entry box and a button.

class Location_Tracker:
    def __init__(self, App):
        # The function creates a window with a text entry box and a button.
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#C6302B")
        self.window.resizable(False, False)

        # ___________Application menu_____________
        # Creating a window with a text entry box and a button.
        Label(App, text="Enter a phone number", fg="white",
              font=("Times", 20), bg="#3f5efb").place(x=150, y=30)
        self.phone_number = Entry(
            App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(
            App, text="Track Country", bg="#22c1c3", relief="sunken")
        self.country_label = Label(
            App, fg="white", font=("Times", 20), bg="#3f5efb")

        # ___________Place widgets on the window______
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)

        # __________Linking button with countries ________
        self.track_button.bind(
            "<Button-1>", self.Track_location)  # 255757294146

    def Track_location(self, event):
        # The function takes the phone number entered in the text box and finds the country of the phone number.
        phone_number = self.phone_number.get()
        # `The country is then displayed on the window`
        country = "Country is Unknown"
        # `The country is then displayed on the window`
        if phone_number:
            tracked = pycountry.countries.get(
                alpha_2=phone_country(phone_number))
            print(tracked)
            if tracked:
                # print(tracked.name)
                if hasattr(tracked, "official_name"):
                    country = tracked.official_name
                    # print(country)
                else:
                    country = tracked.name
        self.country_label.configure(text=country)


# Creating a window and displaying it on the screen.
PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()
