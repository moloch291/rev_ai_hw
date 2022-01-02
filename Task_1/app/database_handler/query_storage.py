from .database_common import connection_handler
# importing magic numbers:
import sys
sys.path.append("..")
from variable_storage import magic_numbers as mgc_n


# Since in the description no one said it is a web app I didn't pay attention to defend against SQL injection!
@connection_handler
def get_avg_per_neighbourhood_groups(cursor):
    cursor.execute("""SELECT n.neighbourhood_group,
                             trunc(avg(l.price)::numeric, 2) as avg_price
                      FROM neighbourhood n
                      JOIN listing l on n.neighbourhood_group = l.neighbourhood_group
                      GROUP BY n.neighbourhood_group
                      ORDER BY avg_price DESC;""")
    return cursor.fetchall()


@connection_handler
def find_most_reviewed(cursor):
    cursor.execute(
        f"SELECT id FROM listing ORDER BY number_of_reviews DESC LIMIT {mgc_n.MAX_REVIEW_LIMIT};"
    )
    return cursor.fetchone()


@connection_handler
def get_avg_of_most_reviewed(cursor, id_of_max_review):
    cursor.execute(
        f"""SELECT
                trunc(avg(split_part(price, '$', {mgc_n.SQL_PRICE_POSITION})::numeric), {mgc_n.SQL_PRICE_POSITION})
                AS avg_price
            FROM calendar
            WHERE listing_id = {id_of_max_review};"""
    )
    return cursor.fetchall()


@connection_handler
def get_unique_response_time(cursor):
    cursor.execute(
        "SELECT DISTINCT host_response_time FROM listing_complex;"
    )
    return cursor.fetchall()


@connection_handler
def count_of_props_w_coffee_m(cursor):
    cursor.execute(
        "SELECT COUNT(*) FROM listing_complex WHERE amenities ~ 'coffee';"
    )
    return cursor.fetchall()
