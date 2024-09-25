
create database VirtualArtGallery;
use VirtualArtGallery;

CREATE TABLE Artists (
 ArtistID INT PRIMARY KEY,
 Name VARCHAR(255) NOT NULL,
 Biography TEXT,
 Nationality VARCHAR(100));

CREATE TABLE Categories (
 CategoryID INT PRIMARY KEY,
 Name VARCHAR(100) NOT NULL);

CREATE TABLE Artworks (
 ArtworkID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 ArtistID INT,
 CategoryID INT,
 Year INT,
 Description TEXT,
 ImageURL VARCHAR(255),
 FOREIGN KEY (ArtistID) REFERENCES Artists (ArtistID),
 FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID));


CREATE TABLE Exhibitions (
 ExhibitionID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 StartDate DATE,
 EndDate DATE,
 Description TEXT);

CREATE TABLE ExhibitionArtworks (
 ExhibitionID INT,
 ArtworkID INT,
 PRIMARY KEY (ExhibitionID, ArtworkID),
 FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
 FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID));

INSERT INTO Artists (ArtistID, Name, Biography, Nationality) VALUES
 (1, 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'),
 (2, 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'),
 (3, 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian');

INSERT INTO Categories (CategoryID, Name) VALUES
 (1, 'Painting'),
 (2, 'Sculpture'),
 (3, 'Photography');

INSERT INTO Artworks (ArtworkID, Title, ArtistID, CategoryID, Year, Description, ImageURL) VALUES
 (1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'),
 (2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'),
 (3, 'Guernica', 1, 1, 1937, 'Pablo Picasso powerful anti-war mural.', 'guernica.jpg');


INSERT INTO Exhibitions (ExhibitionID, Title, StartDate, EndDate, Description) VALUES
 (1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces.'),
 (2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.');


INSERT INTO ExhibitionArtworks (ExhibitionID, ArtworkID) VALUES
 (1, 1),
 (1, 2),
 (1, 3),
 (2, 2);

 /*
 1. Retrieve the names of all artists along with the number of artworks they have in the gallery, and
list them in descending order of the number of artworks
*/
 select Artists.Name , count(Artworks.ArtworkID) as TotalArtworks
 from Artists left join Artworks
 on Artists.ArtistID = Artworks.ArtistID
 group by Artists.Name
 order by TotalArtworks desc;

/*
2. List the titles of artworks created by artists from 'Spanish' and 'Dutch' nationalities, and order
them by the year in ascending order
*/
 select Artworks.Title , Artworks.Year as year
 from Artworks join Artists
 on Artists.ArtistID = Artworks.ArtistID
 where Artists.Nationality in ('Spanish' , 'Dutch')
 order by year;

/*
3. Find the names of all artists who have artworks in the 'Painting' category, and the number of
artworks they have in this category.
*/
 select a.Name , count(aw.ArtworkID) as TotalArtworks
 from Artists a join Artworks aw on a.ArtistID = aw.ArtistID
 JOIN Categories c ON aw.CategoryID = c.CategoryID
 WHERE c.Name = 'Painting'
 GROUP BY a.Name;

/*
4. List the names of artworks from the 'Modern Art Masterpieces' exhibition, along with their
artists and categories.
*/
 select aw.Title, a.Name, c.Name
 from Artworks aw
 join Artists a on aw.ArtistID = a.ArtistID
 join Categories c on aw.CategoryID = c.CategoryID
 join ExhibitionArtworks ea on aw.ArtworkID = ea.ArtworkID
 join Exhibitions e ON ea.ExhibitionID = e.ExhibitionID
 where e.Title = 'Modern Art Masterpieces';


/*
5. Find the artists who have more than two artworks in the gallery
*/
 select a.Name, count(aw.ArtworkID) as TotalArtworks
 from Artists a
 join Artworks aw on a.ArtistID=aw.ArtistID
 group by (a.Name)
 having count(aw.ArtworkID) > 2;

/*
6. Find the titles of artworks that were exhibited in both 'Modern Art Masterpieces' and
'Renaissance Art' exhibitions
*/
 select aw.Title
 from Artworks aw
 where aw.ArtworkID in
 (
	select ea.ArtworkID
	from ExhibitionArtworks ea 
	join Exhibitions e on ea.ExhibitionID = e.ExhibitionID
	where e.Title = 'Modern Art Masterpieces'
 )
 and aw.ArtworkID in
 (
	select ea.ArtworkID
	from ExhibitionArtworks ea 
	join Exhibitions e on ea.ExhibitionID = e.ExhibitionID
	where e.Title = 'Renaissance Art'
 );

/*
7. Find the total number of artworks in each category
*/
 select c.Name as CategoryName, count(aw.ArtworkID) as TotalArtworks
 from Categories c
 left join Artworks aw on c.CategoryID = aw.CategoryID
 group by (c.Name);


 --8. List artists who have more than 3 artworks in the gallery
 select a.Name, count(aw.ArtworkID) as TotalArtworks
 from Artists a
 join Artworks aw on a.ArtistID=aw.ArtistID
 group by (a.Name)
 having count(aw.ArtworkID) > 3;

 --9. Find the artworks created by artists from a specific nationality (e.g., Spanish).
 select a.Name, aw.Title 
 from Artists a
 join Artworks aw on a.ArtistID = aw.ArtistID
 where a.Nationality = 'Spanish';

 --10. List exhibitions that feature artwork by both Vincent van Gogh and Leonardo da Vinci
 select e.Title as ExhibitionName
 from Exhibitions e
 where e.ExhibitionID in
 (
	select ew.ExhibitionID
	from ExhibitionArtworks ew
	join Artworks aw on ew.ArtworkID = aw.ArtworkID
	join Artists a on aw.ArtistID = a.ArtistID
	where a.Name = 'Vincent van Gogh'
 )
 and e.ExhibitionID in
 (
	select ew.ExhibitionID
	from ExhibitionArtworks ew
	join Artworks aw on ew.ArtworkID = aw.ArtworkID
	join Artists a on aw.ArtistID = a.ArtistID
	where a.Name = 'Leonardo da Vinci'
 );


 --11. Find all the artworks that have not been included in any exhibition.
 select Title
 from Artworks
 where ArtworkID not in
 (
	select ArtworkID  from ExhibitionArtworks
 );

--12. List artists who have created artworks in all available categories.
SELECT 
    a.Name AS ArtistName
FROM 
    Artists a
JOIN 
    Artworks aw ON a.ArtistID = aw.ArtistID
JOIN 
    Categories c ON aw.CategoryID = c.CategoryID
GROUP BY 
    a.ArtistID, a.Name
HAVING 
    COUNT(DISTINCT aw.CategoryID) = (SELECT COUNT(*) FROM Categories);



 --13. List the total number of artworks in each category.
 Select c.Name , count(aw.ArtworkID)
 from Categories c
 left join Artworks aw on c.CategoryID=aw.CategoryID
 group by (c.Name);


 --14. Find the artists who have more than 2 artworks in the gallery
 select a.Name, count(aw.ArtworkID) as TotalArtworks
 from Artists a
 join Artworks aw on a.ArtistID=aw.ArtistID
 group by (a.Name)
 having count(aw.ArtworkID) > 2;

 /* 
 List the categories with the average year of artworks they contain, only for categories with more
than 1 artwork.
*/
 select c.Name categoryName, avg(aw.Year)
 from Categories c
 join Artworks aw on c.CategoryID = aw.CategoryID
 group by(c.Name)
 having count(c.Name)>1;

 --16. Find the artworks that were exhibited in the 'Modern Art Masterpieces' exhibition

 select aw.Title
 from Artworks aw
 join ExhibitionArtworks ea on aw.ArtworkID = ea.ArtworkID
 join Exhibitions e on e.ExhibitionID = ea.ExhibitionID
 where e.Title = 'Modern Art Masterpieces';

 --17. Find the categories where the average year of artworks is greater than the average year of all artworks.
 select c.Name
 from Categories c
 join Artworks aw on c.CategoryID = aw.CategoryID
 group by (c.Name)
 having avg( aw.Year ) > (select avg(Year) from Artworks);

 --18. List the artworks that were not exhibited in any exhibition.

 select Title as Name
 from Artworks 
 where ArtworkID not in (
 select ArtworkID from ExhibitionArtworks
 );

 --19. Show artists who have artworks in the same category as "Mona Lisa."

 select a.Name ArtistName
 from Artists a
 join Artworks aw on a.ArtistID = aw.ArtistID
 where aw.CategoryID = ( select CategoryID from Artworks
						 where Title = 'Mona Lisa');

--20. List the names of artists and the number of artworks they have in the gallery.

select a.Name ArtistName, count(aw.ArtworkID)
from Artists a
join Artworks aw on a.ArtistID=aw.ArtistID
group by(a.Name);
