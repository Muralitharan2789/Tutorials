## Power Apps Look Table Query

  <fetch>
  <entity name="new_student">
  <attribute name="new_studentnumberid" />
  <attribute name="new_lessonnumberid" />
  <link-entity name="new_lesson" from="new_lessonnumberid" to="new_lessonnumberid" alias="L">
  <attribute name="new_lessonid" alias="new_lessonid"/>
  </link-entity>
  </entity>
  </fetch>
