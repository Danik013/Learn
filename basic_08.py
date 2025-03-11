import json
import requests
from geopy import distance
from pprint import pprint
import folium


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def get_min_dist(caffee):
    return caffee["distance"]


def main():
    apikey = "d1c4c1e7-9487-4a1d-a23d-2bd51339557c"
    location_а = input("Где вы находитесь? ")
    x, y = fetch_coordinates(apikey, location_а)
    my_coord_location = y, x
    print("Ваши оординаты:", fetch_coordinates(apikey, location_а))
    
    coffee_file = open("coffee.json", "r", encoding="CP1251")
    coffee_list = coffee_file.read()
    all_coffee = json.loads(coffee_list)
    
    dist_all_caffee = []
    for one_caffe in all_coffee:
        dict_one_caffe = dict()
        caffee_coord_geopy = one_caffe["Latitude_WGS84"], one_caffe["Longitude_WGS84"]
        dict_one_caffe["title"] = one_caffe["Name"]
        dict_one_caffe["distance"] = distance.distance(my_coord_location, caffee_coord_geopy).km
        dict_one_caffe["latitude"] = one_caffe["Latitude_WGS84"]
        dict_one_caffe["longitude"] = one_caffe["Longitude_WGS84"]
        dist_all_caffee.append(dict_one_caffe)
    
    sorted_dist_caffee = sorted(dist_all_caffee, key=get_min_dist)
    five_closest_caffe = sorted_dist_caffee[:5]
    
    m = folium.Map(my_coord_location, zoom_start=12)
    
    folium.Marker(
        location=my_coord_location,
        tooltip="Click me!",
        popup="Мое местоположение",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    for count in range(5):
        folium.Marker(
            location=[five_closest_caffe[count]['latitude'], five_closest_caffe[count]['longitude']],
            tooltip="Click me!",
            popup=five_closest_caffe[count]['title'],
            icon=folium.Icon(color="green"),
        ).add_to(m)
    
    m.save("index.html")
    

if __name__ == '__main__':
    main()


