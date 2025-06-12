import React, {useState} from 'react';
export const DocumentsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>DOCUMENTS - Documents - attachments, support letters</h2><p>attachments</p></div>
};
export default DocumentsView;
