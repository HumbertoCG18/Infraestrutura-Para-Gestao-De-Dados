CREATE INDEX IDX_AIRPORTS_GEO_COUNTRY ON AIR_AIRPORTS_GEO(COUNTRY);
CREATE INDEX IDX_FLIGHTS_AIRPORTS ON AIR_FLIGHTS(FROM_AIRPORT_ID, TO_AIRPORT_ID);
CREATE INDEX IDX_AIRPLANES_TYPE ON AIR_AIRPLANES(AIRPLANE_TYPE_ID);