#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import retriever
import parser

## https://www.dmv.virginia.gov/onlineservices/appointments.aspx
## https://www.dmv.virginia.gov/dmvlocations/#/Locations
calendar_ids = {
    "Abingdon":                      3871869, ## 25552 Lee Highway
    "Alexandria":                    4024314, ## 2681 Mill Road
    "Altavista":                     4190268, ## 1301 H Main Street
    "Arlington":                     3871975, ## 4150 South Four Mile Run Drive
    "Arlington Metro at Va. Square": 4190475, ## 3434 North Washington Blvd. Suite RET01
    "Bedford":                       4315670, ## 1128 E. Lynchburg Salem Turnpike
    "Charlottesville":               3886284, ## 2055 Abbey Road
    "Chesapeake":                    3886163, ## 813 Greenbrier Parkway
    "Chester":                       3886184, ## 12100 Branders Creek Drive
    "Chesterfield":                  3875732, ## 610 Johnston Willis Drive
    "Christiansburg":                3886254, ## 385 Arbor Drive
    "Clintwood":                     4190413, ## 2311 Dickenson Hwy
    "Courtland":                     4344158, ## 27426 Southampton Parkway
    "Covington":                     4175348, ## 121 Mall Road
    "Culpeper":                      4190301, ## 18505 Crossroad Parkway
    "Danville":                      4151229, ## 126 Sandy Court, Suite C
    "East Henrico":                  4190274, ## 5517 South Laburnum Avenue
    "Emporia":                       3886231, ## 103 Commonwealth Blvd
    "Fairfax/Westfields":            3885857, ## 14950 Northridge Drive
    "Fair Oaks Mall":                4371716, ## 11805 Fair Oaks Mall
    "Farmville":                     4024330, ## 300 North Virginia Street
    "Franconia":                     3874863, ## 6306 Grovedale Drive
    "Fredericksburg":                3885986, ## 5700 Southpoint Centre Blvd
    "Front Royal":                   4023692, ## 15 Water Street
    "Galax":                         3885798, ## 7565 Carrollton Pike
    "Gate City":                     4085797, ## 382 Jones Street, Suite 101
    "Gloucester":                    3886025, ## 2348 York Crossing Drive
    "Hampton":                       3875052, ## 8109 Roanoke Avenue
    "Harrisonburg":                  3875825, ## 3281 Peoples Drive
    "Hopewell":                      4344236, ## 4401 Crossings Boulevard
    "Jonesville":                    4188688, ## 195 Hill Street
    "Kilmarnock":                    4315621, ## 110 DMV Drive
    "Lebanon":                       4151199, ## 567 W. Main Street
    "Leesburg":                      3885903, ## 945 Edwards Ferry Road NE
    "Lexington":                     4984749, ## 110 East Midland Trail
    "Lorton":                        4315634, ## 7714 Gunston Plaza
    "Lynchburg":                     3963598, ## 3236 Odd Fellows Road
    "Marion":                        4344188, ## 1595 North Main Street
    "Martinsville":                  4023801, ## 310 Starling Avenue
    "Newport News":                  3886076, ## 12730 Patrick Henry Drive
    "Norfolk/Military Circle":       4023752, ## 5745 Poplar Hall Drive
    "Norfolk/Widgeon Road":          4254672, ## 850 Widgeon Road
    "North Henrico":                 3886205, ## 9015 Brook Road
    "Norton":                        4151201, ## 1729 Park Avenue S.W
    "Onancock":                      3875131, ## 20 North Street
    "Petersburg":                    4190448, ## 120 Wagner Road
    "Portsmouth":                    3919119, ## 6400 Bickford Parkway
    "Prince William/Manassas":       3874930, ## 11270 Bulloch Drive
    "Pulaski":                       4315658, ## 1901 Bobwhite Boulevard
    "Richmond Central":              3871785, ## 2300 West Broad Street
    "Roanoke":                       3875799, ## 5220 Valleypark Drive
    "Rocky Mount ":                  4254721, ## 305 Tanyard Road
    "South Boston":                  3920195, ## 2039 Hamilton Blvd
    "South Hill":                    4190378, ## 206 South Brunswick Avenue
    "Stafford":                      4371755, ## 874 Garrisonville Road
    "Staunton":                      4344162, ## 17 First Street
    "Sterling":                      4307275, ## 100 Free Court Sterling
    "Sterling_new":                  4873695, ## S. Sterling Boulevard, Unit D112 (NEW LOCATION)
    "Suffolk":                       4254592, ## 1040 Centerbrooke Lane
    "Tappahannock":                  4175356, ## 750 Richmond Beach Road
    "Tazewell":                      3963741, ## 1151 Tazewell Avenue
    "Tysons Corner":                 3874794, ## 1968 Gallows Road
    "VA Beach-Buckner":              3875641, ## 3551 Buckner Boulevard
    "VA Beach-Hilltop":              4254723, ## 1712 Donna Drive
    "Vansant":                       4175329, ## 1657 Lovers Gap Road
    "Warrenton":                     4254573, ## 94 Alexandria Pike
    "Waynesboro":                    4024243, ## 998 Hopeman Parkway
    "West Henrico":                  4315900, ## 9237 Quioccasin Road
    "Williamsburg":                  4254627, ## 5235 John Tyler Highway
    "Winchester":                    4254601, ## 4050 Valley Pike
    "Woodbridge":                    3886009, ## 2731 Caton Hill Road
    "Woodstock":                     4023824, ## 714-A North Main Street
    "Wytheville":                    4190207, ## 800 East Main Street, Suite 100
}


def main(location=None):
    ## original title with registration
    calendar_type = 14002837

    if location is not None:
        locations = [location]
    else:
        # locations = calendar_ids.keys()
        locations = (
            "Richmond Central",
            "East Henrico",
            "North Henrico",
            "West Henrico",
            "Chesterfield",
            "Chester",
            "Fredericksburg",
            "Hopewell",
            "Petersburg",
            "Farmville",
            "South Hill",
            "Courtland",
            "Charlottesville",
            "Tappahannock",
        )

    availability = []
    for loc in locations:
        print(f"getting dates for {loc}")

        resp = retriever.retrieve_calendar(calendar_ids[loc], calendar_type)
        for dt in parser.parse_doc(resp.text):
            availability.append((loc, dt))

    availability.sort(key=lambda x: x[1])

    for loc, dt in availability[:10]:
        print(f"{loc} {dt} https://vadmvappointments.as.me/schedule.php?calendarID={calendar_ids[loc]}")


if __name__ == "__main__":
    main(*sys.argv[1:])
