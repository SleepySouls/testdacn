SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

CREATE TABLE public.user (
    user_id SERIAL NOT NULL,
	username varchar(45) NOT NULL,
	hashed_password varchar(100) NOT NULL,
    email text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL
);
ALTER TABLE public.user OWNER TO postgres;
--Primary key

ALTER TABLE ONLY public.user
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);

--Unique key
ALTER TABLE ONLY public.user
    ADD CONSTRAINT unique_key UNIQUE (username);

ALTER TABLE ONLY public.user
    ADD CONSTRAINT unique_email UNIQUE (email);

ALTER TABLE ONLY public.user
    ADD CONSTRAINT unique_first_name UNIQUE (first_name);

ALTER TABLE ONLY public.user
    ADD CONSTRAINT unique_last_name UNIQUE (last_name);