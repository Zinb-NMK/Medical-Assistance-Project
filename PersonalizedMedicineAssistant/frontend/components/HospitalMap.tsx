// HospitalMap.tsx
import React from 'react';
import GoogleMapReact from 'google-map-react';

const HospitalMarker = ({ text }) => <div className="text-red-500">📍{text}</div>;

const HospitalMap = ({ hospitals }) => {
  const defaultCenter = { lat: 16.803, lng: 80.3926 }; // Vissannapeta coordinates
  const defaultZoom = 12;

  return (
    <div className="hospital-map h-96 rounded-lg shadow-lg">
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'YOUR_GOOGLE_MAPS_API_KEY' }}
        defaultCenter={defaultCenter}
        defaultZoom={defaultZoom}
      >
        {hospitals.map((hospital, index) => (
          <HospitalMarker
            key={index}
            lat={hospital.lat}
            lng={hospital.lng}
            text={hospital.name}
          />
        ))}
      </GoogleMapReact>
    </div>
  );
};

export default HospitalMap;
