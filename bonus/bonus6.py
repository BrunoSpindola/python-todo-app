contents = ["All carrots are to be sliced longitudinally.",
            "the carrots were reportedly sliced",
            "The slicing process was well present"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)