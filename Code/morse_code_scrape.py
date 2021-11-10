from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/Morse_code"
# Thank you Wikipedia!
html_doc = requests.get(URL).text


class MorseCode:

    def __init__(self):
        self.soup = BeautifulSoup(html_doc, "html.parser")
        self.dict = self.get_dict()

    def get_dict(self):
        # Get symbols for dictionary (Alphabet and Punctuation)

        symbol = ["'"]
        for item in self.soup.select("td b a"):

            if "FractionBar" in item.text:
                symbol.append("/")
            elif "Parenthesis" in item.text:
                if "Open" in item.text:
                    symbol.append("(")
                else:
                    symbol.append(")")
            elif item.text == "Ampersand":
                symbol.append("&")
            elif "Hyphen" in item.text or "Slash" in item.text:
                pass
            elif "," in item.text:
                if "Comma" in item.text:
                    symbol.append(",")
                else:
                    symbol.append(item.text.split(",")[0])
            elif "[" in item.text:
                symbol.append(item.text.split("]")[0][-1])
            else:
                symbol.append(item.text)
        morse_dict = {"Symbol": [symbol[num] for num in range(54)]}

        # Get morse code for each symbol
        code = ["·−−−−·"]
        for item in self.soup.select("div a span b"):
            text = item.text.replace(u"\u200a", "")
            if text == "·−−−−·":
                pass
            else:
                code.append(text.replace(" ", ""))

        morse_dict["Code"] = [code[num] for num in range(54)]
        return morse_dict
