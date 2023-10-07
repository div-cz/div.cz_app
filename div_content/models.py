# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    h1 = models.CharField(db_column='H1', max_length=255)  # Field name made lowercase.
    h2 = models.CharField(db_column='H2', max_length=255)  # Field name made lowercase.
    tagline = models.CharField(db_column='Tagline', max_length=64)
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    youtube = models.CharField(db_column='Youtube', max_length=20, null=True, blank=True)
    img1600 = models.CharField(db_column='Img1600', max_length=255)  # Field name made lowercase.
    img500x500 = models.CharField(db_column='Img500x500', max_length=255)  # Field name made lowercase.
    img400x250 = models.CharField(db_column='Img400x250', max_length=255)  # Field name made lowercase.
    alt = models.CharField(db_column='Alt', max_length=255)  # Field name made lowercase.
    perex = models.CharField(db_column='Perex', max_length=255)  # Field name made lowercase.
    autor = models.CharField(db_column='Autor', max_length=255)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', max_length=50)  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter')  # Field name made lowercase.
    created = models.DateField(db_column='Created')  # Field name made lowercase.
    updated = models.DateField(db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'Article'


class Book(models.Model):
    bookid = models.IntegerField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255)  # Field name made lowercase.
    googleid = models.CharField(db_column='GoogleID', max_length=16, null=True)
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    genreid = models.ForeignKey('Metagenre', models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.
    publisherid = models.ForeignKey('Bookpublisher', models.DO_NOTHING, db_column='PublisherID')  # Field name made lowercase.
    worldid = models.ForeignKey('Metaworld', models.DO_NOTHING, db_column='WorldID')  # Field name made lowercase.
    countryid = models.ForeignKey('Metacountry', models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'Book'


class Bookcomments(models.Model):
    commentid = models.IntegerField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'BookComments'


class Bookcover(models.Model):
    coverid = models.IntegerField(db_column='CoverID', primary_key=True)  # Field name made lowercase.
    bookid = models.IntegerField(db_column='BookID')  # Field name made lowercase.
    cover = models.CharField(db_column='Cover', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'BookCover'


class Bookisbn(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='isbns')
    isbn = models.CharField(max_length=13, unique=True)
    edition = models.CharField(max_length=255, null=True, blank=True)
    publicationyear = models.IntegerField(null=True, blank=True)
    format = models.CharField(max_length=100, null=True, blank=True) # e.g., Hardcover, Paperback, eBook
    language = models.CharField(max_length=100, null=True, blank=True) # e.g., English, Czech
    description = models.TextField(null=True, blank=True)
    coverimage = models.URLField(max_length=200, null=True, blank=True)
    
    class Meta:
        db_table = 'BookISBN'

class Bookpublisher(models.Model):
    publisherid = models.IntegerField(db_column='PublisherID', primary_key=True)  # Field name made lowercase.
    publishername = models.CharField(db_column='PublisherName', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'BookPublisher'


class Bookpurchase(models.Model):
    purchaseid = models.IntegerField(db_column='PurchaseID', primary_key=True)  # Field name made lowercase.
    purchasedate = models.DateField(db_column='PurchaseDate')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'BookPurchase'


class Bookrating(models.Model):
    ratingid = models.IntegerField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'BookRating'


class Characterbook(models.Model):
    bookcharacterid = models.IntegerField(db_column='BookCharacterID')  # Field name made lowercase.
    characterrole = models.CharField(db_column='CharacterRole', max_length=255)  # Field name made lowercase.
    characterid = models.ForeignKey('Charactermeta', models.DO_NOTHING, db_column='CharacterID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'CharacterBook'


class Charactergame(models.Model):
    gamecharacterid = models.IntegerField(db_column='GameCharacterID')  # Field name made lowercase.
    characterrole = models.CharField(db_column='CharacterRole', max_length=255)  # Field name made lowercase.
    characterid = models.ForeignKey('Charactermeta', models.DO_NOTHING, db_column='CharacterID')  # Field name made lowercase.
    gameid = models.ForeignKey('Game', models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.

    class Meta:
        db_table = 'CharacterGame'


class Charactermeta(models.Model):
    characterid = models.IntegerField(db_column='CharacterID', primary_key=True)  # Field name made lowercase.
    charactername = models.CharField(db_column='CharacterName', max_length=255)  # Field name made lowercase.
    characterdescription = models.TextField(db_column='CharacterDescription')  # Field name made lowercase.

    class Meta:
        db_table = 'CharacterMeta'


class Charactermovie(models.Model):
    moviecharacterid = models.IntegerField(db_column='MovieCharacterID')  # Field name made lowercase.
    characterrole = models.CharField(db_column='CharacterRole', max_length=255)  # Field name made lowercase.
    characterid = models.ForeignKey(Charactermeta, models.DO_NOTHING, db_column='CharacterID')  # Field name made lowercase.
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.

    class Meta:
        db_table = 'CharacterMovie'


class Charactertvshow(models.Model):
    tvshowcharacterid = models.IntegerField(db_column='TVShowCharacterID')  # Field name made lowercase.
    characterrole = models.CharField(db_column='CharacterRole', max_length=255)  # Field name made lowercase.
    characterid = models.ForeignKey(Charactermeta, models.DO_NOTHING, db_column='CharacterID')  # Field name made lowercase.
    tvshowid = models.ForeignKey('Tvshow', models.DO_NOTHING, db_column='TVShowID')  # Field name made lowercase.

    class Meta:
        db_table = 'CharacterTVShow'


class Comments(models.Model):
    commentid = models.IntegerField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    comment_date = models.DateField(db_column='CommentDate')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'Comments'


class Creator(models.Model):
    creatorid = models.IntegerField(db_column='CreatorID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=512, null=True, blank=True, unique=True)
    birthdate = models.DateField(db_column='BirthDate', null=True, blank=True)  # Field name made lowercase.
    deathdate = models.DateField(db_column='DeathDate', null=True, blank=True)
    imdbid = models.CharField(db_column='Imdb_id', max_length=16, null=True)
    popularity = models.CharField(db_column='Popularity', max_length=32, null=True)
    img = models.CharField(db_column='IMG', max_length=32, null=True)
    knownfordepartment = models.CharField(db_column='KnownForDepartment', max_length=255, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey('Metacountry', models.DO_NOTHING, db_column='CountryID', null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Creator'


class Creatoringame(models.Model):
    creatoringameid = models.IntegerField(db_column='CreatorInGameID', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Creatorrole', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    gameid = models.ForeignKey('Game', models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='CreatorID')  # Field name made lowercase.

    class Meta:
        db_table = 'CreatorInGame'


class Creatorinmovie(models.Model):
    creatorinmovieid = models.IntegerField(db_column='CreatorInMovieID', primary_key=True)  # Field name made lowercase.
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='CreatorID')  # Field name made lowercase.
    roleid = models.ForeignKey('Creatorrole', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.

    class Meta:
        db_table = 'CreatorInMovie'


class Creatorintvshow(models.Model):
    creatorintvshowid = models.IntegerField(db_column='CreatorInTVShowID', primary_key=True)  # Field name made lowercase.
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='CreatorID')  # Field name made lowercase.
    roleid = models.ForeignKey('Creatorrole', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    tvshowid = models.ForeignKey('Tvshow', models.DO_NOTHING, db_column='TVShowID')  # Field name made lowercase.

    class Meta:
        db_table = 'CreatorInTVShow'


class Creatorrole(models.Model):
    roleid = models.IntegerField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=255)  # Field name made lowercase.
    rolenamecz = models.CharField(db_column='RoleNameCZ', max_length=255, blank=True)
    department = models.CharField(db_column='Department', max_length=255, blank=True)
    class Meta:

        db_table = 'CreatorRole'


class Drink(models.Model):
    drinkid = models.IntegerField(db_column='DrinkID', primary_key=True)  # Field name made lowercase.
    drinkname = models.CharField(db_column='DrinkName', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    class Meta:
        db_table = 'Drink'


class Drinkmedia(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mediatype = models.IntegerField(db_column='MediaType')  # Field name made lowercase.
    drinkid = models.ForeignKey(Drink, models.DO_NOTHING, db_column='DrinkID')  # Field name made lowercase.

    class Meta:
        db_table = 'DrinkMedia'


class Food(models.Model):
    foodid = models.IntegerField(db_column='FoodID', primary_key=True)  # Field name made lowercase.
    foodname = models.CharField(db_column='FoodName', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    class Meta:
        db_table = 'Food'


class Foodmedia(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mediatype = models.IntegerField(db_column='MediaType')  # Field name made lowercase.
    foodid = models.ForeignKey(Food, models.DO_NOTHING, db_column='FoodID')  # Field name made lowercase.

    class Meta:
        db_table = 'FoodMedia'


class Game(models.Model):
    gameid = models.IntegerField(db_column='GameID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    ratingid = models.IntegerField(db_column='RatingID')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    platformid = models.ForeignKey('Gameplatform', models.DO_NOTHING, db_column='PlatformID')  # Field name made lowercase.
    publisherid = models.ForeignKey('Gamepublisher', models.DO_NOTHING, db_column='PublisherID')  # Field name made lowercase.
    genreid = models.ForeignKey('Metagenre', models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.
    worldid = models.ForeignKey('Metaworld', models.DO_NOTHING, db_column='WorldID')  # Field name made lowercase.
    developerid = models.ForeignKey('Gamedevelopers', models.DO_NOTHING, db_column='DeveloperID')  # Field name made lowercase.
    countryid = models.ForeignKey('Metacountry', models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'Game'


class Gamecomments(models.Model):
    commentid = models.IntegerField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'GameComments'


class Gamedevelopers(models.Model):
    developerid = models.IntegerField(db_column='DeveloperID', primary_key=True)  # Field name made lowercase.
    developername = models.CharField(db_column='DeveloperName', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'GameDevelopers'


class Gameplatform(models.Model):
    platformid = models.IntegerField(db_column='PlatformID', primary_key=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=255)  # Field name made lowercase.
    url = models.CharField(db_column='PlatformURL', max_length=255, blank=True)
    class Meta:
        db_table = 'GamePlatform'


class Gamepublisher(models.Model):
    publisherid = models.IntegerField(db_column='PublisherID', primary_key=True)  # Field name made lowercase.
    publishername = models.CharField(db_column='PublisherName', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'GamePublisher'


class Gamepurchase(models.Model):
    purchaseid = models.IntegerField(db_column='PurchaseID', primary_key=True)  # Field name made lowercase.
    purchasedate = models.DateField(db_column='PurchaseDate')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gameid = models.ForeignKey('Game', models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'GamePurchase'


class Gamerating(models.Model):
    ratingid = models.IntegerField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'GameRating'

class Itemtype(models.TextChoices):
    WEAPON = '1', 'Zbraň'
    TOOL = '2', 'Nástroj'
    CLOTHING = '3', 'Oděv'
    VEHICLE = '4', 'Vozidlo'
    DOCUMENT = '5', 'Dokument'
    JEWEL = '6', 'Klenot'
    HOUSEHOLD = '7', 'Domácí potřeby'
    MAGICAL_ITEM = '8', 'Magický předmět'
    ARTEFACT = '9', 'Artefakt'
    OTHER = '10', 'Ostatní'

class Item(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255, unique=True)  # Field name made lowercase.
    itemname_cz = models.CharField(db_column='ItemNameCZ', max_length=255, blank=True)
    itemdescription = models.TextField(db_column='ItemDescription')  # Field name made lowercase.
    itemtype = models.CharField(max_length=3, choices=Itemtype.choices, db_column='ItemType', null=True, blank=True)
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        db_table = 'Item'


class Itembook(models.Model):
    bookitemid = models.IntegerField(db_column='BookItemID', primary_key=True)  # Field name made lowercase.
    itemrole = models.CharField(db_column='ItemRole', max_length=255)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'ItemBook'


class Itemgame(models.Model):
    gameitemid = models.IntegerField(db_column='GameItemID', primary_key=True)  # Field name made lowercase.
    itemrole = models.CharField(db_column='ItemRole', max_length=255)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.

    class Meta:
        db_table = 'ItemGame'


class Itemmovie(models.Model):
    movieitemid = models.IntegerField(db_column='MovieItemID', primary_key=True)  # Field name made lowercase.
    itemrole = models.IntegerField(db_column='ItemRole')  # Field name made lowercase.
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.

    class Meta:
        db_table = 'ItemMovie'


class Itemmediatype(models.TextChoices):
    BOOK = '1', 'Book'
    GAME = '2', 'Game'
    MOVIE = '3', 'Movie'

class Itemmediarole(models.TextChoices):
    MAIN = '1', 'Main'
    SIDE = '2', 'Side'
    PROP = '3', 'Prop'

class Itemmedia(models.Model):
    mediaitemid = models.AutoField(db_column='MediaItemID', primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, db_column='Item')
    mediatype = models.IntegerField(choices=Itemmediatype.choices, db_column='MediaType')
    role = models.IntegerField(choices=Itemmediarole.choices, db_column='Role')
    mediaid = models.IntegerField(db_column='MediaID')  # FK to the specific media, you might need to handle this differently for each type

    class Meta:
        db_table = 'ItemMedia'



class Location(models.Model):
    locationid = models.IntegerField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=255, unique=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='LocationType', max_length=50)  # Field name made lowercase.
    locationdescription = models.TextField(db_column='LocationDescription')  # Field name made lowercase.
    parentlocationid = models.IntegerField(db_column='ParentLocationID', blank=True, null=True)  # Field name made lowercase.
    locationadress = models.CharField(db_column='LocationAdress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Location'


class Locationbook(models.Model):
    booklocationid = models.IntegerField(db_column='BookLocationID', primary_key=True)  # Field name made lowercase.
    locationrole = models.CharField(db_column='LocationRole', max_length=255)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        db_table = 'LocationBook'


class Locationgame(models.Model):
    gamelocationid = models.IntegerField(db_column='GameLocationID', primary_key=True)  # Field name made lowercase.
    locationrole = models.CharField(db_column='LocationRole', max_length=255)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.

    class Meta:
        db_table = 'LocationGame'


class Locationmovie(models.Model):
    movielocationid = models.IntegerField(db_column='MovieLocationID', primary_key=True)  # Field name made lowercase.
    locationrole = models.CharField(db_column='LocationRole', max_length=255)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.

    class Meta:
        db_table = 'LocationMovie'


class Metacity(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True)  # Field name made lowercase.
    namecity = models.CharField(db_column='NameCity', max_length=255)  # Field name made lowercase.
    countryid = models.ForeignKey('Metacountry', models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'MetaCity'

class Metacollection(models.Model):
    collectionid = models.IntegerField(db_column='CollectionID', primary_key=True)
    collectionname = models.CharField(db_column='CollectionName', max_length=255)
    collectiondescription = models.TextField(db_column='CollectionDescription')

    class Meta:
        db_table = 'MetaCollection'

class Metacountry(models.Model):
    countryid = models.IntegerField(db_column='CountryID', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=255)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=4)  # Field name made lowercase.
    countrycode2 = models.CharField(db_column='CountryCode2', max_length=2, blank=True)
    countrynamecz = models.CharField(db_column='CountryNameCZ', max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'MetaCountry'


class Metagenre(models.Model):
    genreid = models.IntegerField(db_column='GenreID', primary_key=True)  # Field name made lowercase.
    genrename = models.CharField(db_column='GenreName', max_length=255)  # Field name made lowercase.
    genrenamecz = models.CharField(db_column='GenreNameCZ', max_length=255)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True, unique=True)
    tmdbid = models.IntegerField(db_column='TmdbID')  # Field name made lowercase.

    class Meta:
        db_table = 'MetaGenre'


class Metaworld(models.Model):
    worldid = models.IntegerField(db_column='WorldID', primary_key=True)  # Field name made lowercase.
    worldname = models.CharField(db_column='WorldName', max_length=255)  # Field name made lowercase.
    worlddescription = models.TextField(db_column='WorldDescription', null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'MetaWorld'

class MovieSpecialSort(models.TextChoices):
    TOP = '1', 'Top'
    CZ = '2', 'CZ'

class Movie(models.Model):
    movieid = models.IntegerField(db_column='MovieID', primary_key=True)  # Field name made lowercase
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    titlecz = models.CharField(db_column='TitleCZ', max_length=255, default='')  # Field name made lowercase.
    special = models.IntegerField(choices=MovieSpecialSort.choices, db_column='Special', blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=255, unique=True)  # Field name made lowercase.
    oldurl = models.CharField(db_column='OldURL', max_length=255, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=255, default='/static/img/filmy/nomovie.jpg')
    description = models.TextField(db_column='Description', null=True)  # Field name made lowercase.
    releaseyear = models.CharField(db_column='ReleaseYear', max_length=4, null=True)  # Field name made lowercase. 
    duration = models.IntegerField(db_column='Duration', null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=5, null=True, blank=True)  # Field
    budget = models.IntegerField(db_column='Budget', null=True)
    adult = models.IntegerField(db_column='Adult', default='0')
    popularity = models.CharField(db_column='Popularity', max_length=6, null=True)
    idcsfd = models.CharField(db_column='ID_Csfd', max_length=16, null=True)
    idimdb = models.CharField(db_column='ID_Imdb', max_length=16, null=True)  # Field name made lowercase.
    iddiv = models.CharField(db_column='ID_DIV', max_length=16, null=True)  # Field name made lowercase.
    worldid = models.ForeignKey(Metaworld, models.DO_NOTHING, db_column='WorldID', null=True, blank=True)

    class Meta:
        db_table = 'Movie'



class Moviecomments(models.Model):
    commentid = models.IntegerField(db_column='CommentID', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieComments'


class Moviecountries(models.Model):
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    countryid = models.ForeignKey(Metacountry, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieCountries'


class Moviecrew(models.Model):
    moviecrewid = models.IntegerField(db_column='MovieCrewID', primary_key=True, unique=True)  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    roleid = models.ForeignKey(Creatorrole, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    characterid = models.ForeignKey(Charactermeta, models.DO_NOTHING, db_column='CharacterID')  # Field name made lowercase.
    peopleid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='PeopleID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieCrew'


class Moviegenre(models.Model):
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    genreid = models.ForeignKey(Metagenre, models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieGenre'


class Movierating(models.Model):
    ratingid = models.IntegerField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieRating'


class Movieversions(models.Model):
    movieversionid = models.IntegerField(db_column='MovieVersionID', primary_key=True)  # Field name made lowercase.
    versionname = models.CharField(db_column='VersionName', max_length=255)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    releasedate = models.DateField(db_column='ReleaseDate')  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieID')  # Field name made lowercase.

    class Meta:
        db_table = 'MovieVersions'


class Tvepisode(models.Model):
    episodeid = models.IntegerField(db_column='EpisodeID', primary_key=True)  # Field name made lowercase.
    episodenumber = models.IntegerField(db_column='EpisodeNumber')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    airdate = models.DateField(db_column='AirDate')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    sessionid = models.ForeignKey('Tvseason', models.DO_NOTHING, db_column='SessionID')  # Field name made lowercase.

    class Meta:
        db_table = 'TVEpisode'


class Tvseason(models.Model):
    sessionid = models.IntegerField(db_column='SessionID', primary_key=True)  # Field name made lowercase.
    seasonnumber = models.IntegerField(db_column='SeasonNumber')  # Field name made lowercase.
    premieredate = models.DateField(db_column='PremiereDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    tvshowid = models.ForeignKey('Tvshow', models.DO_NOTHING, db_column='TVShowID')  # Field name made lowercase.

    class Meta:
        db_table = 'TVSeason'


class Tvshow(models.Model):
    tvshowid = models.IntegerField(db_column='TVShowID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    premieredate = models.DateField(db_column='PremiereDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    genreid = models.ForeignKey(Metagenre, models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.
    countryid = models.ForeignKey(Metacountry, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'TVShow'


class User(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.
    signupdate = models.DateField(db_column='SignUpDate')  # Field name made lowercase.
    lastlogin = models.DateField(db_column='LastLogin')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='IsAdmin')  # Field name made lowercase.
    profilepicture = models.CharField(db_column='ProfilePicture', max_length=255)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio')  # Field name made lowercase.
    countryid = models.ForeignKey(Metacountry, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.

    class Meta:
        db_table = 'User'

