
class Display():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.lines = [""] * 6
        self.blip = True
        self.interval = 400
        self.clear()

    def text(self, text, line):
        if line > 5:
            raise RuntimeError("You may only access lines 0 to 5.")
        self.lines[line] = text
        self.redraw()

    def show_heartbeat(self, show):
        self.blip = bool(show)
        self.redraw()

    def redraw(self):
        
        if self.driver is None:
            return 

        # Clear display.
        self.driver.fill(0)

        # User-defined lines.
        for row in range(6):
            if self.lines[row] != "":
                self.driver.text(self.lines[row], 0, 8 * row)

        # Show result and update things.
        self.driver.show()

    def clear(self):
        if self.driver is None:
            return 

        self.driver.fill(0)
        self.driver.show()
