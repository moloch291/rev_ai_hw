DROP TABLE IF EXISTS neighbourhood;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS calendar;
DROP TABLE IF EXISTS listing;
DROP TABLE IF EXISTS listing_complex;

CREATE TABLE listing (
    id int,
    name text,
    host_id int,
    host_name text,
    neighbourhood_group text,
    neighbourhood_name text,
    latitude float,
    longitude float,
    room_type text,
    price float,
    minimum_nights int,
    number_of_reviews int,
    last_review date,
    reviews_per_month float,
    calculated_host_listings_count int,
    availability_365 int,
    number_of_reviews_ltm int,
    licence varchar
);

CREATE TABLE neighbourhood (
    neighbourhood_group varchar(200),
    neighbourhood_name varchar(200)
);

/* If I would plan to update this database I'd define the 'listing_id' columns
   in the following tables as a foreign key but since I just want to read data,
   here it isn't necessary: */

CREATE TABLE review (
    listing_id int,
    review_date date
);

CREATE TABLE calendar (
    listing_id int,
    day date,
    available boolean,
    price text,
    adjusted_price text,
    minimum_nights int,
    maximum_nights int
);

CREATE TABLE listing_complex(
    id int,
    listing_url text,
    scrape_id bigint,
    last_scraped date,
    name text,
    description text,
    neighborhood_overview text,
    picture_url text,
    host_id int,
    host_url text,
    host_name text,
    host_since date,
    host_location text,
    host_about text,
    host_response_time text,
    host_response_rate text,
    host_acceptance_rate text,
    host_is_superhost boolean,
    host_thumbnail_url text,
    host_picture_url text,
    host_neighbourhood text,
    host_listings_count int,
    host_total_listings_count int,
    host_verifications text,
    host_has_profile_pic boolean,
    host_identity_verified boolean,
    neighbourhood text,
    neighbourhood_cleansed text,
    neighbourhood_group_cleansed text,
    latitude numeric,
    longitude numeric,
    property_type text,
    room_type text,
    accommodates int,
    bathrooms numeric,
    bathrooms_text text,
    bedrooms int,
    beds int,
    amenities text,
    price text,
    minimum_nights int,
    maximum_nights int,
    minimum_minimum_nights int,
    maximum_minimum_nights int,
    minimum_maximum_nights int,
    maximum_maximum_nights int,
    minimum_nights_avg_ntm numeric,
    maximum_nights_avg_ntm numeric,
    calendar_updated date,
    has_availability boolean,
    availability_30 int,
    availability_60 int,
    availability_90 int,
    availability_365 int,
    calendar_last_scraped date,
    number_of_reviews int,
    number_of_reviews_ltm int,
    number_of_reviews_l30d int,
    first_review date,
    last_review date,
    review_scores_rating numeric,
    review_scores_accuracy numeric,
    review_scores_cleanliness numeric,
    review_scores_checkin numeric,
    review_scores_communication numeric,
    review_scores_location numeric,
    review_scores_value numeric,
    license text,
    instant_bookable boolean,
    calculated_host_listings_count int,
    calculated_host_listings_count_entire_homes int,
    calculated_host_listings_count_private_rooms int,
    calculated_host_listings_count_shared_rooms int,
    reviews_per_month numeric
);