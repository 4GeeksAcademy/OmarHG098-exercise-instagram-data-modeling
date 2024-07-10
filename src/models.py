import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(100), unique = True, nullable = False)
    firstname = Column(String(100), nullable = False)
    lastname = Column(String(100), nullable = False)
    email = Column(String(100), unique = True)

     #Relationships
    followers = relationship("Follower", backref= "user_followers")
    posts = relationship("Post", backref="user_posts")
    comment = relationship("Comment", backref="user_comments")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True, nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"))

    #Relationships
    media = relationship("Media", backref= "post_media")
    comments = relationship("Comment", backref = "post_comments")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True, nullable = False)
    comment_text = Column(String(255), nullable = False)
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id")) 

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True, nullable = False)
    type = Column(String(255), nullable = False)
    url = Column(String(255), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id")) 


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
