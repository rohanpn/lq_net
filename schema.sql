CREATE TABLE  "BookDetails" (
    "id" INTEGER NOT NULL PRIMARY KEY,
	"title" CHAR(56) NOT NULL
	);


CREATE TABLE  "UserRequest" (
    "id" INTEGER NOT NULL PRIMARY KEY,
	"book_id" INTEGER NOT NULL,
	"book_title" CHAR(56) NOT NULL,
    "email" CHAR(56) NOT NULL,
	"timestamp" DATETIME NOT NULL DEFAULT(GETDATE())
	);

GO

INSERT INTO BookDetails("title") values ("Godfather");
INSERT INTO BookDetails("title") values ("Introduction to C");
INSERT INTO BookDetails("title") values ("Data Structures and Algorthms");
INSERT INTO BookDetails("title") values ("Machine Learning with R");
INSERT INTO BookDetails("title") values ("john");
INSERT INTO BookDetails("title") values ("alice");
