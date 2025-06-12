import React, {useState} from 'react';
export const TrackingView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>TRACKING - Tracking - 20 simultaneous submissions, </h2><p>Kanban</p></div>
};
export default TrackingView;
