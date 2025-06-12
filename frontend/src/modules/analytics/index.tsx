import React, {useState} from 'react';
export const AnalyticsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>ANALYTICS - Analytics - success rate, funding, trend</h2><p>success rate</p></div>
};
export default AnalyticsView;
