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

CREATE TABLE public.campaign(
    campaign_id SERIAL NOT NULL,
    title text NOT NULL,
    description text NOT NULL,
    goal_amount decimal NOT NULL, 
    raised_amount decimal NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    category text NOT NULL,
    media bytea NOT NULL,
    status boolean,
    user_id integer NOT NULL,
);
ALTER TABLE public.campaign OWNER TO postgres;

ALTER TABLE ONLY public.campaign
    ADD CONSTRAINT camapaign_pkey PRIMARY KEY (campaign_id);
