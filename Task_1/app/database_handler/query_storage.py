from .database_common import connection_handler
# importing magic numbers:
import sys
sys.path.append("..")
from variable_storage import magic_numbers as mgc_n


@connection_handler
def get_avg_per_neighbourhood_groups(cursor):
    cursor.execute(f"""SELECT n.neighbourhood_group,
                              trunc(avg(l.price)::numeric, {mgc_n.SQL_PRICE_POSITION}) AS avg_price
                       FROM neighbourhood n
                       JOIN listing l ON n.neighbourhood_group = l.neighbourhood_group
                       GROUP BY n.neighbourhood_group
                       ORDER BY avg_price DESC;""")
    return cursor.fetchall()


@connection_handler
def get_avg_of_most_reviewed(cursor):
    cursor.execute(
        f"""SELECT trunc(avg(adj_price::money::numeric), 2) AS avg_price
            FROM (
                SELECT replace(c.adjusted_price, '$', '') AS adj_price
                FROM calendar c
                JOIN listing l ON c.listing_id = l.id
                ORDER BY l.number_of_reviews DESC
                LIMIT 365
            ) AS price_365;"""
    )
    return cursor.fetchone()


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
