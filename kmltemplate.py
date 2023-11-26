class KMLTemplate:

    def __init__(self, output):
        self.output = output

    def kml_heading(self):
        with open(self.output, "w") as kml_file:
            kml_file.write('''<?xml version="1.0" encoding="UTF-8"?>                           
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>Untitled</name>
    <gx:CascadingStyle kml:id="__managed_style_2034FF0A6F2D39936D55">
        <Style>
            <IconStyle>
                <scale>1.2</scale>
                <Icon>
                    <href>https://earth.google.com/earth/rpc/cc/icon?color=d32f2f&amp;id=2000&amp;scale=4</href>
                </Icon>
                <hotSpot x="64" y="128" xunits="pixels" yunits="insetPixels"/>
            </IconStyle>
            <LabelStyle>
            </LabelStyle>
            <LineStyle>
                <color>ff2dc0fb</color>
                <width>6</width>
            </LineStyle>
            <PolyStyle>
                <color>40ffffff</color>
            </PolyStyle>
            <BalloonStyle>
                <displayMode>hide</displayMode>
            </BalloonStyle>
        </Style>
    </gx:CascadingStyle>
    <gx:CascadingStyle kml:id="__managed_style_1FA89C18132D39936D55">
        <Style>
            <IconStyle>
                <Icon>
                    <href>https://earth.google.com/earth/rpc/cc/icon?color=d32f2f&amp;id=2000&amp;scale=4</href>
                </Icon>
                <hotSpot x="64" y="128" xunits="pixels" yunits="insetPixels"/>
            </IconStyle>
            <LabelStyle>
            </LabelStyle>
            <LineStyle>
                <color>ff2dc0fb</color>
                <width>4</width>
            </LineStyle>
            <PolyStyle>
                <color>40ffffff</color>
            </PolyStyle>
            <BalloonStyle>
                <displayMode>hide</displayMode>
            </BalloonStyle>
        </Style>
    </gx:CascadingStyle>
    <StyleMap id="__managed_style_079D34E7702D39936D55">
        <Pair>
            <key>normal</key>
            <styleUrl>#__managed_style_1FA89C18132D39936D55</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#__managed_style_2034FF0A6F2D39936D55</styleUrl>
</Pair>
    </StyleMap>
                       ''')

    def kml_coordinates(self, ip, lat, long):
        with open(self.output, "a") as kml_file:
            kml_file.write(f"""
<Placemark>
    <name>{ip}</name>
    <styleUrl>#__managed_style_079D34E7702D39936D55</styleUrl>
    <Point>
        <coordinates>{long},{lat},0</coordinates>
    </Point>
</Placemark>
""")

    def kml_ending(self):
        with open(self.output, "a") as kml_file:
            kml_file.write("""
</Document>
</kml>
""")
