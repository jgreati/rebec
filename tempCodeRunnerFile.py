    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')